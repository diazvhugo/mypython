#!/usr/bin/python
import random

numeros = [9,4,5,3,8]

i = random.randrange(0, 10)
print i

#random.shuffle(items)

a,b = 0, 1
for i in range(0,10):
	print a,
	a,b = b,a + b
