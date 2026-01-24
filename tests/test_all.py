import pytest
import ci_info

def _set_env(vendor, env=None, pr=False):
    """Create an env dict for the given vendor, optionally simulating a PR."""
    env = env or {}

    val = vendor.get("pr") if pr else vendor.get("env")

    if isinstance(val, str):
        env[val] = "1"

    elif isinstance(val, list):
        for ev in val:
            env[ev] = "1"

    elif isinstance(val, dict):
        if "env" in val:
            if "includes" in val:
                env[val["env"]] = val["includes"]
            elif "ne" in val:
                env[val["env"]] = f"not{val['ne']}"
            elif "any" in val:
                env[val["env"]] = val["any"][-1]
        elif "any" in val:
            env[val["any"][-1]] = "1"
        else:
            for k, v in val.items():
                env[k] = v
    return env


@pytest.mark.parametrize("vendor", ci_info.vendors)
def test_ci_detection(vendor):
    """Populate blank env and test CI / PR detection for each vendor."""
    env = {}
    assert ci_info.name(env) is None
    assert ci_info.is_ci(env) is False
    assert ci_info.is_pr(env) is None

    # Set CI env
    env = _set_env(vendor, env)
    detected_name = ci_info.name(env)
    assert detected_name == vendor.get("name")
    assert ci_info.is_ci(env) is True

    # PR not set yet
    if vendor.get("pr"):
        assert ci_info.is_pr(env) is False
        env = _set_env(vendor, env, pr=True)
        info = ci_info.info(env)
        assert info["is_pr"] is True
        assert info["name"] == vendor["name"]
        assert info["is_ci"] is True
    else:
        assert ci_info.is_pr(env) is None
