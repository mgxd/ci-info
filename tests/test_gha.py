"""Test should only pass in Github Actions environment"""

import os
import pytest
import ci_info


@pytest.mark.skipif(not os.getenv("GITHUB_ACTIONS"), reason="Not in GitHub Actions")
def test_gha():
    IS_REAL_PR = bool(
        os.getenv("GITHUB_EVENT_NAME")
        and os.getenv("GITHUB_EVENT_NAME") == "pull_request"
    )
    assert ci_info.name() == "GitHub Actions"
    assert ci_info.is_ci() is True
    assert ci_info.is_pr() == IS_REAL_PR

    assert ci_info.info() == {
        "name": "GitHub Actions",
        "is_ci": True,
        "is_pr": IS_REAL_PR,
    }
