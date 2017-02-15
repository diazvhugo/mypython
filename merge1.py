#!/usr/bin/python

import itertools

a = ['1','2','3']
b = ['4','5','6','7']

def  merge(a,b):
	r = list(itertools.chain(*zip(a, b)))
	return r

r = merge(a,b)
print r
