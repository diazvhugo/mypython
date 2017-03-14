#!/usr/bin/python

numero = int(raw_input("Dame un numero: "))

if numero%2 == 0:
	print "Es par"
	a = numero/2
	print "%d + %d" % (a, a) 
else:
	print "Es impar"
	a = numero/2
	b = a +1
	print "%d + %d" % (a, b) 
