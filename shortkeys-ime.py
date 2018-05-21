#!/usr/bin/python
# -*- coding: UTF-8 -*-

# ************************** IMPORTANT ****************************
# **** Remember to convert the output to Windows CR/LF format! ****
# *****************************************************************

import sys

f = open("shortkeys.txt", "r")
# fo = sys.stdout
fo = open("shortkeys-ime.out", "w")

# Input Fomat: <ITEM NAME>head
# 					body

# Output Format: 
# ['p', 'Are you pretty? :)']

list = []
head = ""

for line in f:
	if line[0:11] == "<ITEM NAME>":
		head = line[11:-2]						# -2 is due to MSDOS newline
	else:
		list.append((head, line[:-2]))		# append to end of list

# sort according to length, in reverse order (longest first)
list2 = sorted(list, key = lambda item: -len(item[0]))

for item in list2:
	fo.write("[\"" + item[0] + " \",\"" + item[1] + " \"],\n")
