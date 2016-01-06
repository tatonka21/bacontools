#!/usr/bin/env python3
# vim:syntax=python:filetype=python:ts=4:sw=4:noet:

# TODO: write module docstring


import os
import sys
import math
import io


__ticks = [' ', '▁', '▂', '▃', '▄', '▅', '▆', '▇', '█']
__ticks_n = len(__ticks)


if __name__ == '__main__':
	prefix = os.path.basename(__file__)
	print(os.path.basename(prefix+': this module is not meant to be run'
		' directly! exiting'))
	exit(1)

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import termdraw.terminal
import termdraw.csv


def __termdraw_print_help(progname):
	__termdraw_help_string_1 = "Usage: "
	__termdraw_help_string_2 = (
		" file.csv\n\n"
		"Draw a human-friendly CLI graph with Unicode symbols.\n"
		"(file parsing is currently WIP)"
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


def __termdraw_draw_graph(stream, width, height, data, interpolate=False,
		solid_graph=True):
	# TODO: implement non-solid graphs
	# TODO: implement point interpolation
	# TODO: write docstring
	# TODO: make public
	if solid_graph:
		__termdraw_draw_solid_graph(stream, width, height, data, interpolate)
	return 0


def __termdraw_draw_solid_graph(stream, width, height, data, interpolate=False):
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


def termdraw_main(args):
	exit_status = 0
	prefix = os.path.basename(__file__)

	if (len(args) <= 1):
		__termdraw_print_help(prefix)
		exit(1)

	if ('-h' in args) or ('--help' in args):
		__termdraw_print_help(prefix)
	exit(0)
