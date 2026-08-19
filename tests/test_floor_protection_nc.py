"""NEGATIVE CONTROL. This test is designed to fail.

Close the PR unmerged once GitHub reports mergeStateStatus BLOCKED.
Do not land this file.
"""


def test_floor_protection_must_block_merge() -> None:
    assert False, "NEGATIVE CONTROL: required tests check must fail"
