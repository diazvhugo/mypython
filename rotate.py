# Enter your code here. Read input from STDIN. Print output to STDOUT

#!/usr/bin/python

string = ['1','2','3','4','5']
limit = len(string)

#for n in range(0,limit):
#        print string[n-1],

def rotate(l, y=4):
   if len(l) == 0:
      return l
   y = y % len(l)    # Why? this works for negative y
   return l[y:] + l[:y]

string2 = rotate(string)

for n in range(0,limit):
    print string2[n],
