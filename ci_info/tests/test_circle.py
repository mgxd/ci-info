import os
import pytest

IS_CIRCLE = os.getenv("CIRCLE") == "true"
IS_REAL_PR = bool(
    os.getenv("CIRCLE_PULL_REQUEST") and
    os.getenv("CIRCLE_PULL_REQUEST") != "false"
)
@pytest.mark.skipif(not IS_CIRCLE, reason="Requires circle-ci build environment")
def test_travis(tmpdir):
    import ci_info

    assert ci_info.name() == "CircleCI"
    assert ci_info.is_ci() is True
    assert ci_info.is_pr() == IS_REAL_PR

    assert ci_info.info() == {
        "name": "CircleCI",
        "is_ci": True,
        "is_pr": IS_REAL_PR
    }
