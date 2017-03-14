#!/usr/bin/env python

logfile = open("log_file", "r") 

wordcount=0
my_word="apple"
for line in logfile:
    if my_word in line.split():
        wordcount += 1

print my_word, wordcount
