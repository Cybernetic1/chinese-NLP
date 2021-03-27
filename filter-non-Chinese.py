#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Input: list with char + etc...
# Output: filter out lines that does not begin with proper Chinese character

import sys

f1 = open("char-rel-freq.txt", "r")
fo = open("char-rel-freq-2.txt", "w")
#fo = sys.stdout

for line in f1:
	c = ord(line[0])
	if (c >= 19968 and c <= 40959) \
		or (c >= 11904 and c <= 12245) \
		or (c >= 13312 and c <= 19903) \
		or (c >= 131072 and c <= 183983):
		fo.write(line)
	else:
		print ("\033[0;32m", line[:-1], "\033[0m")

fo.close()
