import os
from setuptools import setup, find_packages
setup(   
    name=sampleapp,
    version=0.0.1,
    packages=find_packages(exclude=['tests']),
    zip_safe=False)
