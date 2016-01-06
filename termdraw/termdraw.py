#!/usr/bin/env python3
# vim:syntax=python:filetype=python:ts=4:sw=4:noet:

# TODO: write module docstring


import os
import sys
import math
import io


__ticks = [' ', '▁', '▂', '▃', '▄', '▅', '▆', '▇', '█']
__ticks_n = len(__ticks)


__shortopts = ['h']
__longopts = ['help', 'debug']
__max_term_graph_width = 80
__max_term_graph_height = 30


if __name__ == '__main__':
	prefix = os.path.basename(__file__)
	sys.stderr.write(prefix+': this module is not meant to be run'
		' directly! exiting\n')
	exit(1)

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import termdraw.terminal
import termdraw.csv


print_debug_info = False


def __debug_write(str):
	if print_debug_info:
		sys.stderr.write('debug: ' + str)


def __termdraw_print_help(progname):
	__termdraw_help_string_1 = "Usage: "
	__termdraw_help_string_2 = (
		" [options] file.csv\n\n"
		"Draw a human-friendly CLI graph with Unicode symbols.\n"
		"  -h, --help               Print this help message and exit"
	)
	print(__termdraw_help_string_1 + progname + __termdraw_help_string_2)


def __limited(val, min, max):
	if val > max:
		return max
	else:
		if val < min:
			return min
		else:
			return val


def __scale(val, a, b, c, d):
	return 1.0*(c+(d-c)*(val-a)/(b-a))


def __draw_graph(stream, width, height, data, interpolate=False,
		solid_graph=True):
	# TODO: implement non-solid graphs
	# TODO: implement point interpolation
	# TODO: write docstring
	# TODO: make public
	if solid_graph:
		__termdraw_draw_solid_graph(stream, width, height, data, interpolate)
	return 0


def __termdraw_draw_solid_graph(stream, width, height, data, interpolate=False):
	# TODO: enforce 80 character line wrap
	# TODO: move graph, pts initialization to __termdraw_draw_graph
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
		rawx = __limited(__scale(i[0], left, right, 0, width-1), 0, width-1)
		rawy = __limited(__scale(i[1], bottom, top, 0, height-1), 0, height-1)
		pts.append((rawx, rawy))

	for i in pts:
		# FIXME: if several points have same x value, fractional ticks overwrite bottom filler ticks
		graphx = int(__limited(i[0], 0, width-1))
		graphy = int(__limited(i[1], 0, height-1))
		tickval = int(__limited(__scale(i[1]-math.floor(i[1]), 0, 1, 0, __ticks_n), 0, __ticks_n-1))
		if graphy != 0:
			for n in range(graphy):
				graph[height-n-1][graphx] = __ticks[__ticks_n-1]
		graph[height-graphy-1][graphx] = __ticks[tickval]

	for y in graph:
		for x in y:
			stream.write(x)
		stream.write('\n')


def __interpolate_points(pts):
	result = pts
	return result


def __termdraw_get_soft_view_width(termwidth):
	if termwidth >= __max_term_graph_width:
		return __max_term_graph_width
	else:
		return termwidth


def __termdraw_get_soft_view_height(termheight):
	if termheight >= __max_term_graph_height:
		return __max_term_graph_height
	else:
		return termheight


def termdraw_main(args):
	exit_status = 0
	prefix = os.path.basename(__file__)
	args0 = args[0]
	input_files = []
	bare_dash_active = False
	term_width, term_height = termdraw.terminal.get_terminal_size()
	graph_width = __termdraw_get_soft_view_width(term_width)
	graph_height = __termdraw_get_soft_view_height(term_height)

	if (len(args) <= 1):
		__termdraw_print_help(prefix)
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
			if opt[2:] not in __longopts:
				sys.stderr.write(prefix + ': unknown option ' + opt[2:] + '\n')
				exit(1)
			val = opt[2:]
			if val == 'help':
				__termdraw_print_help(prefix)
				exit(0)
			elif val == 'debug':
				print_debug_info = True
			continue
		elif opt.startswith('-'):
			for c in opt[1:]:
				if c not in __shortopts:
					sys.stderr.write(prefix + ': unknown option ' + c + '\n')
					exit(1)
			if 'h' in opt[1:]:
				__termdraw_print_help(prefix)
				exit(0)
			continue
		else:
			input_files.append(opt)

	for f in input_files:
		__debug_write(f)
		rawdata = termdraw.csv.get_csv_data(f)
		data = [(float(t[0]), float(t[1])) for t in (tuple(x) for x in rawdata)]

		for n in data:
			if len(n) != 2:
				sys.stderr.write(prefix + ': invalid CSV data: ' + repr(n) + '\n')
				exit(1)

		sys.stdout.write(f + '\n')
		__draw_graph(sys.stdout, graph_width, graph_height, data)
