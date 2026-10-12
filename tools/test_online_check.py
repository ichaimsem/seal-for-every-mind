"""Regression tests for the online link check, 12 October 2026.

The check used to treat any non-200 as a broken link. Several cited chapters on
chabad.org answer 403 with a Cloudflare challenge while serving the page normally
in a browser, so the build failed on links that were never broken.
"""
import importlib.util
import subprocess
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location("qa", Path(__file__).with_name("qa.py"))
qa = importlib.util.module_from_spec(spec)
spec.loader.exec_module(qa)

CHALLENGE = "HTTP/2 403\r\nserver: cloudflare\r\ncf-mitigated: challenge\r\n\r\n"


class ClassifyTests(unittest.TestCase):
    def test_200_is_ok(self):
        self.assertEqual(qa.classify("200", "", 0)[0], "ok")

    def test_cloudflare_403_is_unverifiable(self):
        verdict, detail = qa.classify("403", "cf-mitigated: challenge", 0)
        self.assertEqual(verdict, "unverifiable")
        self.assertIn("not opened", detail)

    def test_403_without_the_header_is_broken(self):
        self.assertEqual(qa.classify("403", "server: cloudflare", 0)[0], "broken")

    def test_404_is_broken(self):
        self.assertEqual(qa.classify("404", "", 0)[0], "broken")

    def test_500_is_retried_not_called_broken(self):
        self.assertEqual(qa.classify("500", "", 0)[0], "retry")

    def test_transport_error_is_retried(self):
        self.assertEqual(qa.classify("000", "", 56)[0], "retry")
        self.assertEqual(qa.classify("000", "", 28)[0], "retry")

    def test_other_curl_failure_is_broken(self):
        self.assertEqual(qa.classify("", "", 3)[0], "broken")

    def test_a_200_wins_over_a_challenge_header(self):
        self.assertEqual(qa.classify("200", "cf-mitigated: challenge", 0)[0], "ok")


class FetchUrlTests(unittest.TestCase):
    def setUp(self):
        self.calls = []

    def _sequence(self, attempts):
        it = iter(attempts)
        original = qa.curl_once
        original_sleep = qa.time.sleep
        def fake(u):
            self.calls.append(u)
            return next(it)
        qa.curl_once = fake
        qa.time.sleep = lambda s: None
        self.addCleanup(lambda: setattr(qa, "curl_once", original))
        self.addCleanup(lambda: setattr(qa.time, "sleep", original_sleep))

    def test_a_flaky_url_that_recovers_is_not_reported(self):
        self._sequence([("500", "", 0), ("200", "", 0)])
        self.assertEqual(qa.fetch_url("https://example.org/a"), (None, False))
        self.assertEqual(len(self.calls), 2)

    def test_a_url_that_stays_down_is_unchecked_not_dead(self):
        self._sequence([("500", "", 0), ("500", "", 0)])
        problem, unverifiable = qa.fetch_url("https://example.org/a")
        self.assertTrue(unverifiable)
        self.assertIn("after two attempts", problem)

    def test_a_404_is_not_retried(self):
        self._sequence([("404", "", 0)])
        problem, unverifiable = qa.fetch_url("https://example.org/a")
        self.assertFalse(unverifiable)
        self.assertEqual(len(self.calls), 1)


class ArchivePolicyTests(unittest.TestCase):
    """Archive.org is flaky and must not fail the build, but is still never called OK."""

    def setUp(self):
        self.attempts = []
        original = qa.curl_once
        qa.curl_once = lambda u: (self.attempts.append(u), ("404", "", 0))[1]
        original_sleep = qa.time.sleep
        qa.time.sleep = lambda s: None
        self.addCleanup(lambda: setattr(qa, "curl_once", original))
        self.addCleanup(lambda: setattr(qa.time, "sleep", original_sleep))

    def test_archive_404_is_unchecked_not_breakage(self):
        problem, unverifiable = qa.fetch_url("https://web.archive.org/web/1/https://example.org/a")
        self.assertTrue(unverifiable)
        self.assertIn("archive.org answer not trusted", problem)

    def test_archive_is_retried_before_giving_up(self):
        qa.fetch_url("https://web.archive.org/web/1/https://example.org/a")
        self.assertEqual(len(self.attempts), 2)

    def test_a_normal_404_still_fails_and_is_not_retried(self):
        self.attempts.clear()
        problem, unverifiable = qa.fetch_url("https://example.org/gone")
        self.assertFalse(unverifiable)
        self.assertEqual(len(self.attempts), 1)

    def test_an_ordinary_500_is_not_retried_more_than_once(self):
        self.attempts.clear()
        original = qa.curl_once
        qa.curl_once = lambda u: (self.attempts.append(u), ("500", "", 0))[1]
        try:
            problem, unverifiable = qa.fetch_url("https://example.org/slow")
        finally:
            qa.curl_once = original
        self.assertTrue(unverifiable)
        self.assertEqual(len(self.attempts), 2)


class OnlineCheckTests(unittest.TestCase):
    def setUp(self):
        qa.results.clear()

    def _fake_fetch(self, mapping):
        original = qa.fetch_url
        qa.fetch_url = lambda u: mapping[u]
        self.addCleanup(lambda: setattr(qa, "fetch_url", original))

    def test_challenges_alone_warn_and_do_not_fail_the_build(self):
        self._fake_fetch({"https://example.org/a": ("403 bot challenge, not opened https://example.org/a", True)})
        qa.check_online([], urls=["https://example.org/a"])
        status, _, detail = qa.results[-1]
        self.assertEqual(status, "WARN", detail)
        self.assertIn("not opened", detail)

    def test_a_real_breakage_still_fails_even_with_challenges_present(self):
        self._fake_fetch({
            "https://example.org/dead": ("404 https://example.org/dead", False),
            "https://example.org/blocked": ("403 bot challenge, not opened https://example.org/blocked", True)})
        qa.check_online([], urls=["https://example.org/dead", "https://example.org/blocked"])
        status, _, detail = qa.results[-1]
        self.assertEqual(status, "FAIL", detail)
        self.assertIn("/dead", detail)

    def test_everything_opening_is_ok(self):
        self._fake_fetch({"https://example.org/a": (None, False)})
        qa.check_online([], urls=["https://example.org/a"])
        self.assertEqual(qa.results[-1][0], "OK")

    def test_archive_and_issues_urls_are_still_skipped(self):
        self._fake_fetch({})
        qa.check_online([], urls=["https://web.archive.org/save/x", "https://example.org/issues/new"])
        self.assertEqual(qa.results[-1][0], "OK")


if __name__ == "__main__":
    unittest.main()
