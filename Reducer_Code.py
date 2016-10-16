#! /usr/bin/env python

import sys

output = []
for line in sys.stdin:
    line = line.strip()
    title,year,rating,votes = line.split("\t")
    try:
        result = [title, year, rating, votes]				
        output.append(result)								
        #print("\t".join(str(v) for v in result))
    except ValueError:
        pass
final = sorted(output, key=lambda x: int(x[3]), reverse=True)		
for y in final[0:20]:
	print(', '.join(y))
