#!/usr/bin/python
# -*- coding: UTF-8 -*-

# *****************************************************************
# Mix phonetic spelling file and frequency file

import sys

f1 = open("char-phonetics.txt", "r")
f2 = open("char-frequency.txt", "r")

fo = open("char-merged.txt", "w")

# f1 input format:
# char spelling

# f2 input format:
# char frequency

# Output format: 
# char spelling frequency

list = []			# list to store results

# Read file f1 into list
for line in f1:
	# append to end of list
	# -2 is due to MSDOS newline
	list.append((line[0:3], int(line[4:-2])))

# Process file f2
for line in f2:
	char = line[0:3]
	freq = int(line[4:-2])
	# TODO: find index of char in list
	# ....
	# add frequency to list tuple
	list[index] = (list[index][0], list[index][1], freq)

# Print output file
for item in list:
	fo.write("[\"" + item[0] + " \",\"" + item[1] + " \"],\n")

# Bye bye
