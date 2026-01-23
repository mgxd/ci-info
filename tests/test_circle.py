"""Test should only pass in CircleCI environment"""

import os

import pytest

import ci_info


@pytest.mark.skipif(not os.getenv("CIRCLECI"), reason="Not in CircleCI")
def test_circle():
    IS_REAL_PR = bool(
        os.getenv("CIRCLE_PULL_REQUEST") and os.getenv("CIRCLE_PULL_REQUEST") != "false"
    )
    assert ci_info.name() == "CircleCI"
    assert ci_info.is_ci() is True
    assert ci_info.is_pr() == IS_REAL_PR

    assert ci_info.info() == {"name": "CircleCI", "is_ci": True, "is_pr": IS_REAL_PR}
