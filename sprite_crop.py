

import os
import sys

if len(sys.argv) != 6:
  sys.exit(0)

file_name = sys.argv[1]
x1, y1, x2, y2 = sys.argv[2:]
x1 = int(x1)
x2 = int(x2)
y1 = int(y1)
y2 = int (y2)
f = open(file_name, 'r')
lines = []
for l in f.readlines():
  lines.append(l)

lines = lines[y1: y2+1]
for i, l in enumerate(lines):
  lines[i] = l[x1: x2+1]
  if lines[i][-1] == '\n' : 
    lines[i] = lines[i][:-1]

for l in lines:
  print l




