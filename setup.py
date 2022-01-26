from setuptools import setup, find_packages
import glob
import os
import pkg_resources
# Note: the _program variable is set in __init__.py.
# it determines the name of the package/final command line tool.
from pangolin_data import __version__, _program

setup(name='pangolin_data',
      version=__version__,
      packages=find_packages(),
      scripts=[],
      package_data={'pangolin_data':['data/*']},
      description='Data for pangolin assignment',
      url='https://github.com/cov-lineages/pangolin-data',
      author='cov-lineages group',
      author_email='aine.otoole@ed.ac.uk',
      entry_points="""
      [console_scripts]
      {program} = pangolin_data.command:main
      """.format(program = _program),
      include_package_data=True,
      keywords=[],
      zip_safe=False)