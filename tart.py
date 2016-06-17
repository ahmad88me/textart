#!/usr/bin/python

from os import listdir
from os.path import isfile, join
import random
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
mypath = join(BASE_DIR,'textart')
mypath = join(mypath,'9gagtxt')
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
if len(onlyfiles) > 0:
	f = random.randrange(0,len(onlyfiles))
	with open(join(mypath,onlyfiles[f]), 'r') as fin:
    		print fin.read()

