#!/usr/bin/env python3
# vim:syntax=python:filetype=python:ts=4:sw=4:noet:


from __future__ import absolute_import
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from . import graph
from . import csv


def string_wrapper_p2(s):
	if type(s) != unicode:
		return s.decode('utf-8')
	else:
		return s


def string_wrapper_p3(s):
	return s


string_wrapper = string_wrapper_p3 if sys.version_info.major is 3 else\
	string_wrapper_p2


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

		result = ''

		for l in lines[:-1]:
			result += l[0:self.width]
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

		graphfunc = graph.print_solid_graph if self.is_solid else graph.print_point_graph

		self.string = string_wrapper(graphfunc(self.width, self.height,
			self.data, self.interpolate, self.ticks))
		self.trimstring()

		if get_string_region_dimensions(self.string) != (self.width,
				self.height):
			raise ValueError('Rendered graph is not of expected dimensions')


def get_region_dimensions(s):
	'''Accept a list of lines, return maximum width in characters and total
	height in lines.
	'''
	# if type(s) is not list:
		# raise TypeError('oh noe')

	return (max([len(i) for i in s]), len(s))


def get_string_region_dimensions(s):
	'''Accept a newline-separated string, return maximum width in characters
	and total height in lines.
	'''
	isnot = (isinstance(s, basestring))\
		if sys.version_info.major is 2\
		else (type(s) is not str)

	# if isnot:
		# raise TypeError('oh noe')

	tmp = s.split('\n')[:-1]
	return get_region_dimensions(tmp)
