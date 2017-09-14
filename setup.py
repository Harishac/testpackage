import os
from setuptools import setup, find_packages

setup(
    name="hello",
    version="0.13.1",
    packages=['hello'],
    entry_points={'console_scripts': ['hello = __main__:main']},
    zip_safe=False)
