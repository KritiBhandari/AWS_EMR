
#! /usr/bin/env python

import sys
import re

for line in sys.stdin:
	line = line.strip()
	unpacked = line.split(",")
	try:
		num,title,year,length,budget,rating,votes,r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,mpaa,Action,Animation,Comedy,Drama,Documentary,Romance,Short = line.split(",")
		if float(rating) == 1:
			results = [title, year, rating, votes]
			print("\t".join(results))
	except ValueError:
		pass

