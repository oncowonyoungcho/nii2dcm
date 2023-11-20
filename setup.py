from setuptools import setup
from dunamai import Version, Style

setup(
    name="nii2dcm",
    version="0.1.2"#Version.from_git().serialize(metadata=False, style=Style.SemVer),
)
