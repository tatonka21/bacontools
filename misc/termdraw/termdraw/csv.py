#!/usr/bin/env python3
# vim:syntax=python:filetype=python:ts=4:sw=4:noet:

'''Define functions for parsing CSV files
'''

from __future__ import absolute_import
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
	'''Open CSV file, read its contents, return them as a list

	Args:
		filename (string): name of the CSV file to be read

	Returns:
		list of all entries in filename
	'''
	with open(filename, 'r') as csvfile:
		s = csvfile.read()
		if not any(['-' in i for i in s]):
			try:
				dialect = csv.Sniffer().sniff(s)
			except:
				dialect = csv.excel
		else:
			dialect = csv.excel

		csvfile.seek(0)

		reader = csv.reader(csvfile, dialect)
		return list(trim_csv_data(reader))


def get_csv_data_string(s):
	'''Read CSV data from a string, return as a list

	Args:
		s (string): CSV data

	Returns
		list of all entries in s
	'''
	# if not any(['-' in i for i in s]):
		# try:
			# dialect = csv.Sniffer().sniff(tmp)
		# except:
			# dialect = csv.excel
	# else:
		# dialect = csv.excel

	reader = csv.reader(s, delimiter = '\n', quotechar = '"')
	tmp_lst = list(trim_csv_data(reader))
	lst = []

	itr = enumerate(tmp_lst)

	# FIXME: this is a dirty hack because csv somehow separates hyphens from the numbers
	for (i, c) in itr:
		if c[0].startswith('-'):
			if i < len(tmp_lst)-1:
				string = c[0]
				string += next(itr, None)[1][0]
				lst.append([string])
			else:
				sys.stderr.write(os.path.basename(__file__) + ': unable to parse input\n')
				exit(1)
				pass
		else:
			lst.append(c)

	return lst


def trim_csv_data(data):
	'''Delete empty entries from the tuple list

	Args:
		data (list[tuple]): source CSV data

	Returns:
		the same list but with empty entries filtered out
	'''
	for t in data:
		if len(t) is not 0:
			yield t


def trim_csv_string(s):
	'''Delete empty lines from the line list

	Args:
		s (list[str]): source CSV data as lines

	Returns:
		the same list but with empty lines filtered out
	'''
	for t in s:
		if len(t.strip()) is not 0:
			yield t


def infer_data_schema(data):
	'''Detect what kind of data is received.

	Args:
		data(list[tuple]): source CSV data

	Returns:
		str: "points" if the data is of form (x,y), "values", if it's of
		     form (y), "mixed", if it's both, "unknown" otherwise
	'''
	single = False
	double = False
	unknown = False

	for t in data:
		if (len(t) is 1):
			try:
				float(t[0])
				single = True
			except:
				unknown = True
		elif (len(t) is 2):
			try:
				float(t[0])
				float(t[1])
				double = True
			except:
				unknown = True
		else:
			unknown = True

	if not unknown:
		if single:
			if double:
				return "mixed"
			else:
				return "values"
		elif double:
			return "points"
	else:
		return "unknown"
