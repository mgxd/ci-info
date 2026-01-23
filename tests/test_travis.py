"""Test should only pass in travis-ci environment"""

import os
import pytest
import ci_info


@pytest.mark.skipif(not os.getenv("TRAVIS"), reason="Not in Travis CI")
def test_travis():
    IS_REAL_PR = bool(
        os.getenv("TRAVIS_PULL_REQUEST") and os.getenv("TRAVIS_PULL_REQUEST") != "false"
    )

    assert ci_info.name() == "Travis CI"
    assert ci_info.is_ci() is True
    assert ci_info.is_pr() == IS_REAL_PR

    assert ci_info.info() == {"name": "Travis CI", "is_ci": True, "is_pr": IS_REAL_PR}
