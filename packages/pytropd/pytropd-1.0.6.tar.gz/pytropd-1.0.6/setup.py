#!/usr/bin/env python

# PyTropD installation script
from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README')) as f:
      long_description = f.read()

setup (name="pytropd",
	version="1.0.6",
        description = "Calculation of metrics of tropical width",
	long_description=long_description,
        license = "GPL-3",
        author="Alison Ming, Paul William Staten",
        author_email="admg26@gmail.com",
        url="https://tropd.github.io/pytropd/index.html",
	requires=['numpy','matplotlib','scipy'],
        install_requires=['numpy>=1.12.0'],
        python_requires=">=3.5",
	packages=["pytropd"],
        classifiers=["Programming Language :: Python :: 3"],
)

