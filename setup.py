import os
from setuptools import setup, find_packages

setup(
    name=os.getenv('PKG_NAME', ''),
    version=os.getenv('PKG_VERSION', ''),
    packages=find_packages(exclude=['tests']),
    zip_safe=False)
