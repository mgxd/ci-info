from setuptools import setup
import versioneer


if __name__ == "__main__":
    setup(
        name="ci",
        version=versioneer.get_version(),
        cmdclass=versioneer.get_cmdclass(),
    )
