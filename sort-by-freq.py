#!/usr/bin/python
# -*- coding: UTF-8 -*-

# *** Unfinished as of 2021

# Notice that by pinyin I mean spellings for Cantonese.

# Input: list1 with char + pinyin
#		 list2 with char + freq
# Output: sort list1 by freq looked up from list2

import sys

if len(sys.argv) != 3:
	print("Usage: sort-by-freq input freq-file output")
	print("input-file format: 字 + ....\\n")
	print("freq-file format: 字 + freq\\n")
	print("output-file: sort input by freq looked up from freq-file")
	exit(0)

# f1 = open("canto-jyutping.txt", "r")	# format: char \b pinyin with tone number
f1 = open("../conceptual-keyboard/web/exact-Google-pinyins.txt", "r")
f2 = open("canto-raw.txt", "r")			# format: char, freq
# fo = sys.stdout
fo = open("canto-sort-by-freq.txt", "w")

big_sum = 0
freq_sum = 0
last_pinyin = "a"							# note: this must be the first pinyin in list

pinyins = []

for line in f1:
	pinyins.append(line.split(' '))

for line in f2:
	items = line.split(',')
	# print line

	char = items[0]
	# freq = float(items[1][:-1])

	found = False
	for item in pinyins:
		if char == item[0]:
			fo.write(char + ',' + item[1])
			found = True

	if not found:
		print char, " not found!!"

	if False: """
	# remove tone number at the end
	if pinyin_tone[-1].isdigit():
		# tone = '0'
		pinyin = pinyin_tone[:-1]
	else:
		pinyin = pinyin_tone
	"""

	# fo.write('[\'' + k + '\',\'' + n + '\',%.9f],\n' % freq_sum)
