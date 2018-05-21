import sys
fo = sys.stdout

n = 0
for i in range(1, 23):
	for j in range(0, i):
		fo.write("{0},".format(n))
		n += 1
	fo.write("\n");

fo.write("\nend\n");
