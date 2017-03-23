#!/usr/bin/python

import re

file='/home/vict9977/Python_test/access.log'
regexp = '^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

match = []

##################################################
for line in open(file):
	match.append(line.split()) 

for i in range(0, len(match)-1):
	print match[i][1]

##################################################
for line in open(file):
	ip = re.findall( r'[0-9]+(?:\.[0-9]+){3}', line )
	print ip

##################################################
ipPattern = re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')

for line in open(file):
	findIP = re.findall(ipPattern,line)
	print findIP
