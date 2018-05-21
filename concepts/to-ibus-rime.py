#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import string
import re

# print "The file database_default.txt will be converted to .yaml for iBus-Rime"
# if raw_input("'Y' to proceed? ") != 'Y':
#	exit()

# Output format:
# phrase <tab> key-sequence \n

# fo = sys.stdout
fo = open('/home/yky/.config/ibus/rime/concepts.dict.yaml', 'w')

# print header
f = open('dict.yaml.header.txt', 'r')
for line in f:
	fo.write(line)

f = open('indexed.txt', 'r')

def num2alpha(num):
	return chr(num / 26 + ord('a')) + chr(num % 26 + ord('a'))

for line in f:
	# fo.write("****** " + line)
	line = line[:-1]
	if line[0] == '\t':			# this is a heading line
		# get heading level = number of periods '.'
		# level = line.count('.')
		# get heading
		match = re.search("\t([A-Z\.]*) (.*)", line)
		heading = match.group(2)
		label = match.group(1)
		label = label.replace('.', '')
		label = label.lower()
		# label = "a" + label

		fo.write(heading + "\t" + label + "\n")

	else:
		match = re.search("([0-9]*) (.*)", line)
		number = int(match.group(1))
		alpha = num2alpha(number)
		item = match.group(2)
		fo.write(item + "\t" + label + alpha + "\n")
		# print "Inserted item: %s" % doc

f.close()

# re-format file as json array
#os.system("sed 's/}$/},/; 1s/^{/[{/; $s/},$/}]/' test.json > db/conkey_db.json")
#print "JSON formated as array and copied to db/conkey_db.json"

exit()
