"""Pure illustrative policy gate; does not perform real operations or grant live access."""
from dataclasses import dataclass
from typing import FrozenSet

@dataclass(frozen=True)
class Grant:
    principal: str
    task: str
    resource: str
    action: str
    approved: bool = False

HIGH_IMPACT = frozenset({"read_private", "write_data", "send_message", "delete_data"})
ACTIONS = HIGH_IMPACT | {"read_public"}

def allowed(principal: str, task: str, resource: str, action: str,
            grants: FrozenSet[Grant], human_approved: bool = False) -> bool:
    if any(not isinstance(x, str) or not x or x != x.strip() or x == "*"
           for x in (principal, task, resource, action)):
        return False
    if action not in ACTIONS:
        return False
    matches = [g for g in grants if (g.principal, g.task, g.resource, g.action)
               == (principal, task, resource, action)]
    if not matches:
        return False
    if action in HIGH_IMPACT and not (human_approved and any(g.approved for g in matches)):
        return False
    return True
