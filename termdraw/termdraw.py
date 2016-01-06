#!/usr/bin/env python3
# vim:syntax=python:filetype=python:ts=4:sw=4:noet:

# TODO: write module docstring


import os
import sys
import math
import io
import itertools


_ticks = [' ', '▁', '▂', '▃', '▄', '▅', '▆', '▇', '█']
_ticks_n = len(_ticks)


_shortopts = ['h', 'i', 'n']
_longopts = ['help', 'debug', 'interpolate', 'no-interpolate']
_max_term_graph_width = 80
_max_term_graph_height = 30


if __name__ == '__main__':
	prefix = os.path.basename(__file__)
	sys.stderr.write(prefix+': this module is not meant to be run'
		' directly! exiting\n')
	exit(1)

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import termdraw.terminal
import termdraw.csv
from termdraw.interpolate import linear_interpolate

print_debug_info = False


def _termdraw_print_help(progname):
	_termdraw_help_string_1 = "Usage: "
	_termdraw_help_string_2 = (
		" [options] file.csv\n\n"
		"Draw a human-friendly CLI graph with Unicode symbols.\n"
		"  -h, --help               Print this help message and exit\n"
		"  -i, --interpolate        Enable interpolation\n"
		"  -n, --no-interpolate     Disable interpolation"
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
	return 1.0*(c+(d-c)*(val-a)/(b-a))


def _draw_graph(stream, width, height, data, interpolate=True,
		solid_graph=True):
	# TODO: implement non-solid graphs
	# TODO: write docstring
	# TODO: make public
	if solid_graph:
		_termdraw_draw_solid_graph(stream, width, height, data, interpolate)
	return 0


def _termdraw_draw_solid_graph(stream, width, height, data, interpolate=True):
	# TODO: enforce 80 character line wrap
	# TODO: move graph, pts initialization to _termdraw_draw_graph
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
		rawx = int(_limited(_scale(i[0], left, right, 0, width-1), 0, width-1))
		rawy = _limited(_scale(i[1], bottom, top, 0, height-1), 0, height-1)
		pts.append((rawx, rawy))

	if interpolate:
		pts = _interpolate_points(pts)

	pts = _deduplicate_points(pts)

	for i in pts:
		graphx = int(_limited(i[0], 0, width-1))
		graphy = int(_limited(i[1], 0, height-1))
		tickval = int(_limited(_scale(i[1]-math.floor(i[1]), 0, 1, 0, _ticks_n), 0, _ticks_n-1))
		if graphy != 0:
			for n in range(graphy):
				graph[height-n-1][graphx] = _ticks[_ticks_n-1]
		graph[height-graphy-1][graphx] = _ticks[tickval]

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


def _termdraw_get_soft_view_width(termwidth):
	if termwidth >= _max_term_graph_width:
		return _max_term_graph_width
	else:
		return termwidth


def _termdraw_get_soft_view_height(termheight):
	if termheight >= _max_term_graph_height:
		return _max_term_graph_height
	else:
		return termheight


def _main(args):
	exit_status = 0
	prefix = os.path.basename(__file__)
	global print_debug_info
	args0 = args[0]
	input_files = []
	bare_dash_active = False
	interpolate = True
	term_width, term_height = termdraw.terminal.get_terminal_size()
	graph_width = _termdraw_get_soft_view_width(term_width)
	graph_height = _termdraw_get_soft_view_height(term_height)

	if (len(args) <= 1):
		_termdraw_print_help(prefix)
		exit(1)

	args.pop(0)

	for opt in args:
		if opt == '--':
			if bare_dash_active == False:
				bare_dash_active == True
				continue
			else:
				input_files.append(opt)
		elif bare_dash_active:
			input_files.append(opt)
			continue
		elif opt.startswith('--'):
			if opt[2:] not in _longopts:
				sys.stderr.write(prefix + ': unknown option ' + opt[2:] + '\n')
				exit(1)
			val = opt[2:]
			if val == 'help':
				_termdraw_print_help(prefix)
				exit(0)
			elif val == 'debug':
				print_debug_info = True
			elif val == 'interpolate':
				interpolate = True
			elif val == 'no-interpolate':
				interpolate = False
			continue
		elif opt.startswith('-'):
			val = opt[1:]
			for c in val:
				if c not in _shortopts:
					sys.stderr.write(prefix + ': unknown option ' + c + '\n')
					exit(1)
			if 'h' in val:
				_termdraw_print_help(prefix)
				exit(0)
			if 'i' in val:
				interpolate = True
			if 'n' in val:
				interpolate = False
			continue
		else:
			input_files.append(opt)

	for f in input_files:
		_debug_write(f)
		rawdata = termdraw.csv.get_csv_data(f)
		data = [(float(t[0]), float(t[1])) for t in (tuple(x) for x in rawdata)]

		for n in data:
			if len(n) != 2:
				sys.stderr.write(prefix + ': invalid CSV data: ' + repr(n) + '\n')
				exit(1)

		sys.stdout.write(f + '\n')
		_draw_graph(sys.stdout, graph_width, graph_height, data,
				interpolate=interpolate)
