#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Input: list with char + freq + etc...
# Output: normalized frequencies

import sys

f1 = open("cantonese/WHK-char-freq.csv", "r")
fo = sys.stdout
# fo = open("canto-sort-by-freq.txt", "w")

# **** Calculate total frequency
freq_sum = 0

for line in f1:
	freq = int(line.split(',')[1])
	freq_sum += freq

print("Total frequency = ", freq_sum)

# **** Output relative frequencies

f1.seek(0)
for line in f1:
	items = line.split(',')
	char = items[0]
	freq = int(items[1])
	relative_freq = freq / freq_sum

	fo.write(char + ',%.12f\n' % relative_freq)

fo.close()
