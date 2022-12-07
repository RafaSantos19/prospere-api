"""Setup file"""
from setuptools import setup, find_packages

with open("requirements.txt") as rf:
    requirements = rf.readlines()

setup(
    name="",
    url="",
    author=[""],
    author_email=[""],
    description="",
    version="",
    python_requires=">3.9",
    install_requires=requirements,
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    test_suite="tests",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    long_description=open('README.md', 'r').read(),
)