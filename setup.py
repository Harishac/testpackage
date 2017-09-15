from setuptools import setup, find_packages

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='hellon',
      version='0.1.0',
      description='test',
      url='https://github.com/Harishac/testpackage',
      author='hac',
      author_email='hac@test.com',
      license='test',
      #long_description=readme(),
      # https://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'License :: Other/Proprietary License',
          'Programming Language :: Python :: 2.7',
          'Topic :: Scientific/Engineering :: Artificial Intelligence',
          'Intended Audience :: Science/Research',
      ],
      keywords='hello',
      packages=['hello'],
      #packages=find_packages(),
      #test_suite='nose.collector',
      #tests_require=['nose'],
      include_package_data=True,
      zip_safe=False)
