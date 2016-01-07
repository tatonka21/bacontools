#!/usr/bin/env python3
# vim:syntax=python:filetype=python:ts=4:sw=4:noet:

import os
from setuptools import setup

setup(
	name = 'termdraw',
	version = '0.1-alpha',
	author = 'Ilya Terentyev',
	author_email = 'bacondropped@gmail.com',
	description = 'Utility library for textual data visualization',
	license = 'MIT',
	keywords = 'data graph ascii visualization',
	url = 'https://github.com/bacondropped/termdraw',
	packages = ['termdraw'],
	scripts = ['bin/termdraw'],
	classifiers = [
		"Environment :: Console",
		"Intended Audience :: Developers",
		"Intended Audience :: Science/Research",
		"License :: Freely Distributable",
		"Programming Language :: Python :: 3 :: Only",
		"Topic :: Scientific/Engineering :: Visualization",
		"Topic :: Utilities"
	]
)
