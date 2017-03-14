#!/usr/bin/python

numeros = [1,2,2,8,8,4,4,3,1]

duplicado=0
for n in numeros:
	duplicado = 0
	for i in range(0,len(numeros)):
		if n == numeros[i]:
			duplicado = duplicado + 1
	if duplicado == 2 :
		print "duplicado %d" % duplicado
	else:
		a = n
		print "unico %d" % duplicado
print a
