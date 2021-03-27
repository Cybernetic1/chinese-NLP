#!/usr/bin/python
# -*- coding: UTF-8 -*-

# *****************************************************************
# Merge 2 files with possibly common chars
# add their frequencies together (with weights)

import sys

f1 = open("cantonese/CUHK-rel-freq.txt", "r")
total1 = 11825308
f2 = open("cantonese/WHK-rel-freq.txt", "r")
total2 = 2943956
total = total1 + total2

#fo = open("rel-freq-merged.txt", "w")
fo = sys.stdout

# f1 input format:
# char,freq

# f2 input format:
# char,freq

# Output format: 
# char,freq

dic = {}		# dictionary

# **** Read file f1 into dictionary
for line in f1:
	if line[0] == '/':
		continue
	items = line.split(',')
	char1 = items[0]
	freq1 = float(items[1])
	dic[char1] = (freq1 * total1) / total

# **** Process file f2
for line in f2:
	if line[0] == '/':
		continue
	
	items = line.split(',')
	char2 = items[0]
	freq2 = float(items[1])

	if char2 in dic:
		# common in both files:
		# add frequencies together
		freq0 = dic[char2]
		# print (line[:-1], "%.10f" % freq0)
		dic[char2] = freq0 + (freq2 * total2) / total
	else:
		# unique to file-2:
		dic[char2] = (freq2 * total2) / total
		# print ("\033[0;35m", line[:-1], "\033[0m")

# **** Print output file
for d in dic:
	fo.write(d + ',%.12f\n' % dic[d])

# Bye bye
