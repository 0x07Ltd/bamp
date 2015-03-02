import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="bumper",
    version="0.0.1",
    author="Ellis Percival",
    author_email="bumper@failcode.co.uk",
    description="A simple command line tool to bump a version number, create "
        "a tag, and push changes to a git server.",
    license="UNLICENSE",
    keywords="git setup.py bump version",
    url="https://github.com/flyte/bumper",
    packages=("bumper",),
    install_requires=read("requirements.txt"),
    entry_points={
        "console_scripts": (
            "bumper = bumper.tool:main",
        )
    }
)
