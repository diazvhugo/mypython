#!/usr/bin/python

file = '/home/hugo/Test/text.txt'

def contar(word):
	count = 0
	for i in open(file):
		for j in i.split():
			if word == j:
				count = count + 1
	return count

if __name__ == '__main__':
	word=raw_input("Dime una palabra: ")
	print contar(word)
