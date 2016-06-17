#!/usr/bin/python

from os import listdir
from os.path import isfile, join
import random
import os

import sys
from time import sleep

if len(sys.argv) != 2:
	print 'expects file name without extension'
	sys.exit(0)	
fname = sys.argv[1]
#print 'fname: '+fname
if os.fork() != 0:
	num_of_files = 0
	for i in range(1, 100):
		exact_fname = fname+str(i)+'.txt'
		if os.path.exists(exact_fname):
			num_of_files = i
		else:
			break
	#print 'num_of_files: '+str(num_of_files)
	for i in range(1, num_of_files+1):
		exact_fname = fname+str(i)+'.txt'
		with open(exact_fname, 'r') as fin:
			print fin.read()
		sleep(0.15)
else:
	os.system("afplay "+fname+".mp3")

