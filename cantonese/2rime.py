#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Convert to iBus-rime (input method) format

import sys

f1 = open("yale.js", "r")	# format: ['spelling',tone,'char',freq],
# fo = sys.stdout
fo = open("yale.yaml", "w")	# format: char <tab> spelling <tab> freq

for line in f1:
	items = line.split(',')
	# print line

	spelling = items[0][2:-1]
	tone = items[1]
	char = items[2][1:-1]
	freq = items[3][:-1]

	fo.write(char + '\t' + spelling + '\t' + freq + '\n')
