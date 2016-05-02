#!/usr/bin/env python3
# vim:syntax=python:filetype=python:ts=4:sw=4:noet:

from __future__ import absolute_import
import os
import sys
import math
import io
import itertools

version_string="0.2.dev1"

_max_term_graph_width = 80
_max_term_graph_height = 30

_shortopts = ['i', 'n', 's', 'p', 'a', 'o', 'w', 'h']
_longopts = ['help', 'debug', 'interpolate', 'no-interpolate', 'solid',
	'point', 'ascii', 'output', 'width', 'height', 'print-paths']
_shortopts_with_arg = ['o', 'w', 'h']
_longopts_with_arg = ['output', 'width', 'height']
_shortlong_map = {
	'i': 'interpolate',
	'n': 'no-interpolate',
	's': 'solid',
	'p': 'point',
	'a': 'ascii',
	'o': 'output',
	'w': 'width',
	'h': 'height'
}


if __name__ == '__main__':
	prefix = os.path.basename(__file__)
	sys.stderr.write(prefix+': this module is not meant to be run'
		' directly! exiting\n')
	exit(1)


sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from . import terminal
from . import csv
from . import cli
from . import graph
from . import view

print_debug_info = False


def _termdraw_print_help(progname):
	_termdraw_help_string_0 = 'termdraw '
	_termdraw_help_string_1 = '\nUsage: '
	_termdraw_help_string_2 = (
		' [options] file.csv\n'
		'Draw a human-friendly CLI graph with Unicode symbols.\n\n'
		'  --help                   Print this help message and exit\n'
		'  -w X, --width X          Limit graph width to X characters\n'
		'  -h Y, --height Y         Limit graph height to Y lines\n'
		'  -i, --interpolate        Enable interpolation\n'
		'  -n, --no-interpolate     Disable interpolation\n'
		'  -s, --solid              Draw solid graph (with columns)\n'
		'  -p, --point              Draw point graph (with points)\n'
		'  -a, --ascii              Only use ASCII symbols\n'
		'  -o file, --output file   Write to file instead of stdout\n'
		'  --print-paths            Print file names before graphs'
	)
	print(
		_termdraw_help_string_0 + version_string +
		_termdraw_help_string_1 + progname + _termdraw_help_string_2)


def _debug_write(str):
	if print_debug_info:
		sys.stderr.write(os.path.basename(__file__) + ': debug: ' + str + '\n')


def _err(str):
	sys.stderr.write(os.path.basename(__file__) + ': ' + str + '\n')


def _draw_graph(stream, width, height, data, interpolate=None,
		solid_graph=True, ascii_only=False):
	graph_view = view.GraphView()
	intp = None
	datatype = csv.infer_data_schema(data)

	if interpolate is None:
		if solid_graph:
			intp = True
		else:
			intp = False
	else:
		intp = interpolate

	if ascii_only:
		solid_graph_ticks = graph.solid_graph_ticks_ascii
		point_graph_tick = graph.point_graph_tick_ascii
	else:
		solid_graph_ticks = graph.solid_graph_ticks_unicode
		point_graph_tick = graph.point_graph_tick_unicode

	_debug_write("_draw_graph received data of type " + repr(datatype))

	if datatype is "mixed" or datatype is "unknown":
		_err("_draw_graph: unable to process received data: incorrect schema")
		exit(1)

	if datatype is "values":
		data = [(str(i), t[0]) for (i, t) in enumerate(data)]

	data = [(float(t[0]), float(t[1])) for t in data]

	graph_view.width = width
	graph_view.height = height
	graph_view.bind_data(data)
	graph_view.interpolate = intp

	if solid_graph:
		graph_view.is_solid = True
		graph_view.ticks = solid_graph_ticks
	else:
		graph_view.is_solid = False
		graph_view.ticks = point_graph_tick

	graph_view.write()
	stream.write(graph_view.string)

def _get_soft_view_width(termwidth):
	if termwidth >= _max_term_graph_width:
		return _max_term_graph_width
	else:
		return termwidth


def _get_soft_view_height(termheight):
	if termheight >= _max_term_graph_height:
		return _max_term_graph_height
	else:
		return termheight


def main():
	args = sys.argv
	exit_status = 0
	global print_debug_info
	args0 = args[0]
	prefix = os.path.basename(__file__)
	output_stream = sys.stdout
	interpolate = True
	term_width, term_height = terminal.get_terminal_size()

	cliparse = cli.CLIParser()
	cliparse.shortoptlist = _shortopts
	cliparse.longoptlist = _longopts
	cliparse.shortopts_with_arg = _shortopts_with_arg
	cliparse.longopts_with_arg = _longopts_with_arg
	cliparse.short_long_mapping = _shortlong_map
	cliparse.accept_bare_dash = True

	if (len(args) <= 1):
		_termdraw_print_help(prefix)
		exit(1)

	try:
		cliparse.parse(args)
	except ValueError as e:
		_err(str(e))
		exit(1)

	print_debug_info = cliparse.longoptions.get('debug', False)

	_debug_write('short CLI options: ' + repr(cliparse.shortoptions))
	_debug_write('long CLI options: ' + repr(cliparse.longoptions))
	_debug_write('raw CLI arguments: ' + repr(cliparse.rawargs))

	input_files = cliparse.rawargs

	opt_interpolate = cliparse.longoptions.get('interpolate', None)
	opt_no_interpolate = cliparse.longoptions.get('no-interpolate', None)
	ascii_only = cliparse.longoptions.get('ascii', False)
	output = cliparse.longoptions.get('output')
	print_paths = cliparse.longoptions.get('print-paths')
	graph_width = int(cliparse.longoptions.get('width',
			_get_soft_view_width(term_width)))
	graph_height = int(cliparse.longoptions.get('height',
			_get_soft_view_height(term_height)))
	opt_solid = cliparse.longoptions.get('solid', None)
	opt_point = cliparse.longoptions.get('point', None)

	if cliparse.longoptions.get('help', False):
		_termdraw_print_help(prefix)
		exit(0)

	if opt_solid is None and opt_point is None:
		solid = True

	if opt_solid is True and opt_point is True:
		_err('both types of graphs have been specified')
		exit(1)

	solid = False if opt_solid is None else True

	if opt_interpolate is None and opt_no_interpolate is None:
		_debug_write('no interpolation option set, selecting ' + repr(solid))
		interpolate = solid

	interpolate = (True if opt_interpolate is not None else False)

	if output is not None:
		if os.path.exists(output):
			_err('file system entry already exists: ' + output)
			exit(1)
		else:
			output_stream = open(output, 'w+')

	if graph_width < 1:
		_err('graph width too small')
		exit(1)

	if graph_height < 1:
		_err('graph height too small')
		exit(1)

	for f in input_files:
		data = []
		is_stdin = False

		if f is '-':
			is_stdin = True

		_debug_write('processing '+(('file '+f) if not is_stdin else 'stdin'))

		if is_stdin:
			stdin_string = sys.stdin.read()
			stdin_string = stdin_string.replace(';', '\n')
			stdin_string = stdin_string.replace(' ', '\n')
			stdin_string = stdin_string.strip()
			rawdata = csv.get_csv_data_string(stdin_string)

		else:
			if not os.path.exists(f):
				_err('file '+f+' does not exist, exiting')
				exit(1)

			rawdata = csv.get_csv_data(f)

		if print_paths:
			output_stream.write(f + '\n')

		_draw_graph(output_stream, graph_width, graph_height, rawdata,
				interpolate, solid, ascii_only)
