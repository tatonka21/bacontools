#!/usr/bin/env python3
# vim:syntax=python:filetype=python:ts=4:sw=4:noet:


from __future__ import absolute_import
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from . import graph
from . import csv


class TextView(object):
	def __init__(self):
		self.width = 0
		self.height = 0

	def write(self, lines, trim=True, include_newline=False):
		raise NotImplementedError('calling TextView.write(); TextView is an '\
		'abstract class')


class StringView(TextView):
	def __init__(self):
		self.width = 0
		self.height = 0
		self.string = ''

	def trimstring(self, trim=True):
		lines = self.string.split('\n')

		if lines[len(lines)-1] is '':
			lines = lines[:len(lines)-1]

		result = ''

		for l in lines:
			result += l[:self.width] if trim else l
			result += '\n'

		self.string = result


class GraphView(StringView):
	def __init__(self):
		self.width = 0
		self.height = 0
		self.source = 0
		self.data = []
		self.string = ''
		self.is_solid = None
		self.interpolate = None
		self.ticks = None

	def bind_data(self, data):
		self.data = data

	def bind_input_file(self, filename, output=None):
		self.source = filename

	def write(self):
		if self.data is []:
			raw_data = [tuple(x) for x in csv.get_csv_data(self.source)]
			self.data = [(float(t[0]), float(t[1])) for t in raw_data]

		if self.is_solid:
			self.string = graph.print_solid_graph(self.width,
			self.height, self.data, self.interpolate, self.ticks)
			self.trimstring()

		else:
			self.string = graph.print_point_graph(self.width,
			self.height, self.data, self.interpolate, self.ticks)
			self.trimstring()
