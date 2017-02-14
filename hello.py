#!/usr/bin/python

nombre = raw_input("nombre: ")
print ("hola "+nombre)

if nombre == 'victor':
 	print ("damn")
else:
 	print ("right")

number = 0
for number in range(1,10):
	result = number % 3
	if result == 0:
		print "tres"

	result = number % 5
	if result == 0:
		print "cinco"

		
