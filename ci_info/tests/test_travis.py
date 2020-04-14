import os
import pytest

IS_TRAVIS = os.environ.get("TRAVIS") == "true"
IS_REAL_PR = bool(
    os.environ.get("TRAVIS_PULL_REQUEST") and
    os.environ.get("TRAVIS_PULL_REQUEST") != "false"
)
@pytest.mark.skipif(not IS_TRAVIS, reason="Requires travis build environment")
def test_travis(tmpdir):
    import ci_info

    assert ci_info.name() == "Travis CI"
    assert ci_info.is_ci() is True
    assert ci_info.is_pr() == IS_REAL_PR

    assert ci_info.info() == {
        "name": "Travis CI",
        "is_ci": True,
        "is_pr": IS_REAL_PR
    }
