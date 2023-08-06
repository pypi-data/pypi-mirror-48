import re

from setuptools import setup

with open("src/pyodstibmivb/__init__.py", "r") as fd:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', fd.read(), re.MULTILINE
    ).group(1)

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="pyodstibmivb",
    version=version,
    author="Emil Vanherp",
    author_email="emil@vanherp.me",
    description="A Python wrapper for the Stib-Mivb opendata API",
    license="MIT License",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/EmilV2/pyodstibmivb",
    install_requires=["aiohttp==3.5.4"],
    python_requires=">=3",
    packages=["pyodstibmivb"],
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
