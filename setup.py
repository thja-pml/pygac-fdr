from setuptools import find_packages, setup


requires = ['numpy', 'netCDF4', 'pygac >=1.3.1', 'satpy >=0.21.0']
test_requires = ['pytest']
README = open('README.md', 'r').read()
setup(name='pygac-fdr',
      description='Python package for creating a Fundamental Data Record (FDR) of AVHRR GAC data '
                  'using pygac',
      long_description=README,
      author='The Pytroll Team',
      author_email='pytroll@googlegroups.com',
      url="https://github.com/pytroll/satpy",
      packages=find_packages(),
      use_scm_version=True,
      install_requires=requires,
      tests_require=test_requires,
      python_requires='>=3.6',
      )
