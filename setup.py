#!/usr/bin/env python3
# vim:syntax=python:filetype=python:ts=4:sw=4:noet:

import os, shutil, sys
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

# Install manpages
# TODO: remove manpages on uninstall
# FIXME: setup will fail on Windows systems; ignore manpages when on Windows
if 'install' in sys.argv:
	man_path = '/usr/share/man/man1/'
	if os.path.exists(man_path):
		print("Installing man pages to " + man_path)
		man_page = "docs/termdraw.1"
		shutil.copy2(man_page, man_path)
		os.chmod(man_path + 'termdraw.1', int('644', 8))
