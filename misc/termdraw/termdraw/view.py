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
		raise NotImplementedError('calling TextView.write(); TextView is an abstract class')


class StringView(TextView):
	def __init__(self):
		self.width = 0
		self.height = 0
		self.outputstring = ''

	def writestring(self, lines, trim=True, include_newline=False):
		self.outputstring = ''

		for l in lines:
			total_len = 0

			if include_newline:
				total_len += 1

			for c in characters:
				if trim and (total_len + len(c) >= self.width):
					break
				else:
					total_len += len(c)
					self.outputstring += c

			self.outputstring += '\n'

	def write(self, lines, trim=True, include_newline=False):
		self.writestring(lines, trim, include_newline)


class WritableBackedView(StringView):
	def __init__(self):
		self.width = 0
		self.height = 0
		self.source = None
		self.output = None
		self.outputstring = ''

	def write(self, lines, trim=True, include_newline=False):
		self.writestring(self, lines, trim, include_newline)
		self.output.write(self.outputstring)


class GraphView(WritableBackedView):
	def __init__(self):
		self.width = 0
		self.height = 0
		self.source = 0
		self.outputstring = ''
		self.is_solid = None
		self.interpolate = None
		self.ticks = None

	def bind_input_file(self, filename, output=None):
		self.source = filename

		if output is not None:
			self.output = output

	def write(self):
		raw_data = [tuple(x) for x in csv.get_csv_data(self.source)]
		data = [(float(t[0]), float(t[1])) for t in raw_data]

		if self.is_solid:
			graph.print_solid_graph(self.output, self.width,
				self.height, data, self.interpolate, self.ticks)
		else:
			graph.print_point_graph(self.output, self.width,
				self.height, data, self.interpolate, self.ticks)
