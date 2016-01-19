#!/usr/bin/env python3
# vim:syntax=python:filetype=python:ts=4:sw=4:noet:

# TODO: write module docstring


import math


def linear_interpolate(a, b, pos):
	return a + (b-a)*pos
