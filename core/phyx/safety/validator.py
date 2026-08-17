"""Safety checks for structured actions.

The v0.1 validator is intentionally conservative. It provides a domain-level
boundary between planning and execution; hardware-specific safety controls
must remain outside this layer as an additional safety mechanism.
"""

from __future__ import annotations

from phyx.actions import Action


class SafetyValidator:
    """Validate actions before they are allowed into an execution layer."""

    def validate(self, action: Action) -> bool:
        """Return True when an action passes basic domain validation."""
        if not action.name.strip():
            return False
        if action.name.lower() in {"disable_safety", "bypass_safety"}:
            return False
        return True
