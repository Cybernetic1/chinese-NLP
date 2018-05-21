#!/usr/bin/python
# -*- coding: utf-8 -*-

# Change the index numbering scheme of Synonym Forest .txt

import sys
import os
import string

f = open('synonym_forest_YKY_database.txt', 'r')
stdout = sys.stdout

current_label = 1
parents = []
current_level = -1
i = 1
max_n = 0
max_i = 0

# The numbering scheme is:
# a,b,c,...,z,
# 1a,1b,1c,...,1z,
# ....
# 9a,9b,9c,...,9z.
# So the maximum number representable is 9z = 260
# Each "number" always ends with an alphabet letter.
# It's regular expression is [1-9]?[a-z]
def num2alpha(n):
	global max_n
	if n > max_n:
		max_n = n
	if n > 260:
		raise NameError("Index overflow: " + str(n))
	n -= 1
	c1 = chr(n / 26 + ord('0'))
	c0 = chr(n % 26 + ord('a'))
	if c1 == '0':
		return c0
	return c1 + c0

for line in f:
	# stdout.write("****** " + line)
	line = line[:-1]
	if line[0] == '\t':			# this is a heading line
		# get heading level = number of periods '.'
		level = line.count('.')
		# get heading
		heading = string.lstrip(line, '\t0123456789. ')
		# level has increased?
		if level == current_level:
			current_label += 1
			parents[-1] = current_label
			i = 1
		elif level > current_level:
			current_label = 1
			parents.append(current_label)
			i = 1
		elif level < current_level:
			parents = parents[0 : level]
			current_label = parents[-1] + 1
			parents[-1] = current_label
			i = 1
		stdout.write('\t')
		for p in parents:
			stdout.write(num2alpha(p) + '.')
		stdout.write(' ' + heading + '\n')
	else:
		items = line.split(' ')		# changed from '|' to space
		# add items to current parent
		for item in items:
			print i, item
			if i > max_i:
				max_i = i
			i += 1

	current_level = level
	# print grand_parents
	
f.close()

print "maximum n is: ", max_n
print "maximum i is: ", max_i
exit()
