from setuptools import setup, find_packages
from pip.req import parse_requirements
from pip.exceptions import InstallationError

try:
    requirements = parse_requirements("requirements.txt")
    install_requires = [str(r.req) for r in requirements]
except InstallationError:
    install_requires = []

try:
    long_description = open("README.rst").read()
except IOError:
    long_description = ""

setup(
    name="smart-tuber",
    version="0.1.0",
    description="Get latest video upload name of smart home youtubers",
    license="MIT",
    author="andrewstech",
    packages=find_packages(),
    install_requires=install_requires,
    long_description=long_description
)
