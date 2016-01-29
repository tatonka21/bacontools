#!/usr/bin/env python3
# vim:syntax=python:filetype=python:ts=4:sw=4:noet:


from __future__ import absolute_import
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from . import graph
from . import csv


class TextView(object):
	'''An abstract base class for all termdraw views.

	Views represent rectangular character areas, which can be bound to some
	data (for instance, a graph). Typically, one calls view.write() and
	retrieves view.string any time when graph should be parsed.

	Attributes:
		width (int):               Width of the view in characters.
		height (int):              Height of the view in lines.
	'''
	def __init__(self):
		self.width = 0
		self.height = 0

	def write(self, lines, trim=True, include_newline=False):
		'''Parse relevant data and write it somewhere.

		This method is expected to be implemented in child classes.
		'''
		raise NotImplementedError('calling TextView.write(); TextView is an '\
		'abstract class')


class StringView(TextView):
	'''A string view, containing a string (hooray).

	Attributes:
		width (int):  Width of the view in characters.
		height (int): Height of the view in lines.
		string (str): Contents of the view as a single string.
	'''
	def __init__(self):
		self.width = 0
		self.height = 0
		self.string = ''

	def trimstring(self):
		'''Trim contents of the graph to fit into a width*height block.
		'''
		lines = self.string.split('\n')

		if lines[len(lines)-1] is '':
			lines = lines[:len(lines)-1]

		result = ''

		for l in lines:
			result += l[:self.width] if trim else l
			result += '\n'

		self.string = result


class GraphView(StringView):
	'''A string view bound to a graph

	Attributes:
		width (int):           Width of the view in characters.
		height (int):          Height of the view in lines.
		source (str):          File name of graph's source.
		data (list[tuple]):    Graph data.
		string (str):          Graph contents as a string.
		is_solid (Boolean):    Type of the graph.
		interpolate (Boolean): Interpolation of the graph.
		ticks (list[str]):     Graph symbols.

	'''
	def __init__(self):
		self.width = 0
		self.height = 0
		self.source = ''
		self.data = []
		self.string = ''
		self.is_solid = None
		self.interpolate = None
		self.ticks = None

	def bind_data(self, data):
		'''Specify graph data for the view.

		Args:
			data (list[tuple]): graph data in form of (x,y) points.
		'''
		self.data = data

	def bind_input_file(self, filename):
		'''Specify file for pulling CSV data from.

		Args:
			filename (str): File path that contains the CSV data.
		'''
		self.source = filename

	def write(self):
		'''Parse the data, draw a graph, and save it to self.string.
		'''
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
