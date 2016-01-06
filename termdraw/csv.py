#!/usr/bin/env python3
# vim:syntax=python:filetype=python:ts=4:sw=4:noet:

# TODO: write module docstring

import os
import sys
import io
import csv


if __name__ == '__main__':
	prefix = os.path.basename(__file__)
	sys.stderr.write(prefix+': this module is not meant to be run'
		' directly! exiting\n')
	exit(1)


def get_csv_data(filename):
	with open(filename, 'r') as csvfile:
		dialect = csv.Sniffer().sniff(csvfile.read(1024))
		csvfile.seek(0)
		reader = csv.reader(csvfile, dialect)
		return list(reader)
