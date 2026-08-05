import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

import pytest

from nuclear_agent.security import PermissionDenied, PermissionPolicy
from nuclear_agent.memory import LocalMemoryStore


def test_permission_policy_allows_analysis_and_denies_control_or_network():
    policy = PermissionPolicy(role="analyst", local_only=True)

    policy.require("simulate_transport")
    policy.require("retrieve_local_knowledge")
    with pytest.raises(PermissionDenied, match="operational_control"):
        policy.require("operational_control")
    with pytest.raises(PermissionDenied, match="external_network"):
        policy.require("external_network")


def test_permission_policy_redacts_sensitive_fields_recursively():
    policy = PermissionPolicy(role="analyst", local_only=True)
    sanitized = policy.redact_payload(
        {
            "scenario_id": "safe-id",
            "operator_name": "Sensitive Name",
            "nested": {"exact_coordinates": "45.0, 9.0", "value": 3},
        }
    )

    assert sanitized["scenario_id"] == "safe-id"
    assert sanitized["operator_name"] == "[REDACTED]"
    assert sanitized["nested"]["exact_coordinates"] == "[REDACTED]"
    assert sanitized["nested"]["value"] == 3


def test_local_memory_is_persistent_session_scoped_and_redacted(tmp_path):
    store = LocalMemoryStore(tmp_path / "memory.jsonl")
    store.add_turn(
        "session-a",
        role="user",
        content="Compare the two potassium cases",
        metadata={"operator_name": "Sensitive Name", "scenario_id": "demo"},
    )
    store.add_turn("session-b", role="user", content="Other session")

    restored = LocalMemoryStore(tmp_path / "memory.jsonl")
    turns = restored.recent("session-a", limit=5)

    assert len(turns) == 1
    assert turns[0]["content"] == "Compare the two potassium cases"
    assert turns[0]["metadata"]["operator_name"] == "[REDACTED]"
    assert restored.recent("session-b", limit=5)[0]["content"] == "Other session"
