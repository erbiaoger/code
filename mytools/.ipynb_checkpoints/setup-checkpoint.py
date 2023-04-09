"""
This is a sample script to handle somethings

Author: Zhang Zhiyu
Email: erbiaoger@gmail.com
Created: 2023/4/9 10:45
Version: 0.0.1

Description:
- My own tools, easy to handle somethings


Usage:
from mytools.mytools import *
from mytools.plot import *

Change Log:
- April 10, 2023, added a new data processing function

"""

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name="mytools",
      version='0.1',
      description='some tools made by erbiaoger',
      url='https://github.com/erbiaoger/code/mytools',
      author='Zhang Zhiyu',
      author_email='erbiaoger@gmail.com',
      # packages=["mytools"],
      packages=find_packages(),
      zip_safe=False,
      install_requires=[
          "numpy",
          "pandas"
          ],
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          ],
      )
