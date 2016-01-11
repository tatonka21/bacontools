#!/usr/bin/env python3
# vim:syntax=python:filetype=python:ts=4:sw=4:noet:

# TODO: write module docstring


import os
import sys
import math
import io
import itertools


_solid_graph_ticks_unicode = [' ', '▁', '▂', '▃', '▄', '▅', '▆', '▇', '█']
_solid_graph_ticks_ascii = [' ', '.', '|']
_point_graph_tick_unicode = '•'
_point_graph_tick_ascii = 'o'

_max_term_graph_width = 80
_max_term_graph_height = 30

_shortopts = ['h', 'i', 'n', 's', 'p', 'a', 'o']
_longopts = ['help', 'debug', 'interpolate', 'no-interpolate', 'solid',
	'point', 'ascii', 'output']
_shortopts_with_arg = ['o']
_longopts_with_arg = ['output']
_shortlong_map = {
	'h': 'help',
	'i': 'interpolate',
	'n': 'no-interpolate',
	's': 'solid',
	'p': 'point',
	'a': 'ascii',
	'o': 'output'
}


if __name__ == '__main__':
	prefix = os.path.basename(__file__)
	sys.stderr.write(prefix+': this module is not meant to be run'
		' directly! exiting\n')
	exit(1)

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import termdraw.terminal
import termdraw.csv
import termdraw.cli
from termdraw.interpolate import linear_interpolate

print_debug_info = False


def _termdraw_print_help(progname):
	_termdraw_help_string_1 = "Usage: "
	_termdraw_help_string_2 = (
		" [options] file.csv\n"
		"Draw a human-friendly CLI graph with Unicode symbols.\n\n"
		"  -h, --help               Print this help message and exit\n"
		"  -i, --interpolate        Enable interpolation\n"
		"  -n, --no-interpolate     Disable interpolation\n"
		"  -s, --solid              Draw solid graph (with columns)\n"
		"  -p, --point              Draw point graph (with points)\n"
		"  -a, --ascii              Only use ASCII symbols\n"
		"  -o file, --output file   Write to file instead of stdout"
	)
	print(_termdraw_help_string_1 + progname + _termdraw_help_string_2)


def _debug_write(str):
	if print_debug_info:
		sys.stderr.write('debug: ' + str)


def _unique_everseen(iterable, key=None):
    "List unique elements, preserving order. Remember all elements ever seen."
    # unique_everseen('AAAABBBCCDAABBB') --> A B C D
    # unique_everseen('ABBCcAD', str.lower) --> A B C D
    seen = set()
    seen_add = seen.add
    if key is None:
        for element in filterfalse(seen.__contains__, iterable):
            seen_add(element)
            yield element
    else:
        for element in iterable:
            k = key(element)
            if k not in seen:
                seen_add(k)
                yield element


def _limited(val, min, max):
	if val > max:
		return max
	else:
		if val < min:
			return min
		else:
			return val


def _scale(val, a, b, c, d):
	return _limited(1.0*(c+(d-c)*(val-a)/(b-a)), c, d)


def _draw_graph(stream, width, height, data, interpolate=None,
		solid_graph=True, ascii_only=False):
	# TODO: write docstring
	# TODO: make public
	intp = None
	if interpolate is None:
		if solid_graph:
			intp = True
		else:
			intp = False
	else:
		intp = interpolate

	if ascii_only:
		solid_graph_ticks = _solid_graph_ticks_ascii
		point_graph_tick = _point_graph_tick_ascii
	else:
		solid_graph_ticks = _solid_graph_ticks_unicode
		point_graph_tick = _point_graph_tick_unicode

	if solid_graph:
		_draw_solid_graph(stream, width, height, data, intp, solid_graph_ticks)
	else:
		_draw_point_graph(stream, width, height, data, intp, point_graph_tick)
	return 0


def _draw_solid_graph(stream, width, height, data, interpolate, ticks):
	ticks_n = len(ticks)
	# Get min and max X and Y values
	left = min(data, key=lambda p: p[0])[0]
	right = max(data, key=lambda p: p[0])[0]
	bottom = min(data, key=lambda p: p[1])[1]
	top = max(data, key=lambda p: p[1])[1]

	# Initialize graph table
	graph = [[' ' for x in range(width)] for y in range(height)]

	# Initialize points list
	pts = []

	for i in data:
		rawx = int(_scale(i[0], left, right, 0, width-1))
		rawy = _scale(i[1], bottom, top, 0, height-1)
		pts.append((rawx, rawy))

	if interpolate:
		pts = _interpolate_points(pts)

	pts = _deduplicate_points(pts)

	for i in pts:
		graphx = int(_limited(i[0], 0, width-1))
		graphy = int(_limited(i[1], 0, height-1))
		tickval = int(_scale(i[1]-math.floor(i[1]), 0, 1, 0, ticks_n-1))
		if graphy != 0:
			for n in range(graphy):
				graph[height-n-1][graphx] = ticks[ticks_n-1]
		graph[height-graphy-1][graphx] = ticks[tickval]

	for y in graph:
		for x in y:
			stream.write(x)
		stream.write('\n')


def _draw_point_graph(stream, width, height, data, interpolate, tick):
	# Get min and max X and Y values
	left = min(data, key=lambda p: p[0])[0]
	right = max(data, key=lambda p: p[0])[0]
	bottom = min(data, key=lambda p: p[1])[1]
	top = max(data, key=lambda p: p[1])[1]

	# Initialize graph table
	graph = [[' ' for x in range(width)] for y in range(height)]

	pts = []

	for i in data:
		rawx = int(_scale(i[0], left, right, 0, width-1))
		rawy = _scale(i[1], bottom, top, 0, height-1)
		pts.append((rawx, rawy))

	if interpolate:
		pts = _deduplicate_points(pts)
		pts = _interpolate_points(pts)

	for i in pts:
		graphx = i[0]
		graphy = int(i[1])
		graph[height-graphy-1][graphx] = tick

	for y in graph:
		for x in y:
			stream.write(x)
		stream.write('\n')


def _deduplicate_points(pts):
	sorted_list = pts

	sorted_list.sort(key=lambda p: p[1], reverse=True)

	uniques = _unique_everseen(sorted_list, key=lambda p: p[0])

	return list(uniques)


def _interpolate_points(pts):
	result = sorted(pts, key=lambda p: p[0])
	_debug_write(repr(result))

	for i, current in enumerate(result):
		if i == (len(result)-1):
			break

		next = result[i+1]

		interval = int(next[0]-current[0])
		a = current[1]
		b = next[1]

		if interval <= 1:
			continue
		for n in range(interval-1):
			newx = current[0] + n + 1
			newy = linear_interpolate(a, b, 1.0*(n+1)/interval)
			result.append((newx, newy))

	_debug_write(repr(result))
	return sorted(result)


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


def _main(args):
	exit_status = 0
	prefix = os.path.basename(__file__)
	global print_debug_info
	args0 = args[0]
	output_stream = sys.stdout
	term_width, term_height = termdraw.terminal.get_terminal_size()
	graph_width = _get_soft_view_width(term_width)
	graph_height = _get_soft_view_height(term_height)

	cliparse = termdraw.cli.CLIParser()
	cliparse.shortoptlist = _shortopts
	cliparse.longoptlist = _longopts
	cliparse.shortopts_with_arg = _shortopts_with_arg
	cliparse.longopts_with_arg = _longopts_with_arg
	cliparse.short_long_mapping = _shortlong_map
	cliparse.accept_bare_dash = True

	if (len(args) <= 1):
		_termdraw_print_help(prefix)
		exit(1)

	# TODO: refactor error messages
	try:
		cliparse.parse(args)
	except ValueError as e:
		sys.stderr.write(str(e)+'\n')
		exit(1)

	print_debug_info = cliparse.longoptions.get('debug', False)

	_debug_write('short CLI options: ' + repr(cliparse.shortoptions))
	_debug_write('long CLI options: ' + repr(cliparse.longoptions))
	_debug_write('raw CLI arguments: ' + repr(cliparse.rawargs))

	input_files = cliparse.rawargs

	interpolate = cliparse.longoptions.get('interpolate')
	no_interpolate = cliparse.longoptions.get('no-interpolate')
	solid = cliparse.longoptions.get('solid', False)
	solid = not cliparse.longoptions.get('point', True)
	ascii_only = cliparse.longoptions.get('ascii', False)
	output = cliparse.longoptions.get('output')

	if interpolate is None and no_interpolate is None:
		_debug_write('no interpolation option set, selecting ' + repr(solid))
		interpolate = solid

	if cliparse.longoptions.get('help', False):
		_termdraw_print_help(prefix)
		exit(0)

	if interpolate and not solid:
		sys.stderr.write(prefix + ': unable to interpolate point graph\n')
		exit(1)

	if output is not None:
		if os.path.exists(output):
			_err('file system entry already exists: ' + output)
			exit(1)
		else:
			output_stream = open(output, 'w+')

	for f in input_files:
		_debug_write(f)
		rawdata = termdraw.csv.get_csv_data(f)
		data = [(float(t[0]), float(t[1])) for t in (tuple(x) for x in rawdata)]

		for n in data:
			if len(n) != 2:
				sys.stderr.write(prefix + ': invalid CSV data: ' + repr(n) + '\n')
				exit(1)

		output_stream.write(f + '\n')
		_draw_graph(output_stream, graph_width, graph_height, data,
				interpolate, solid, ascii_only)
