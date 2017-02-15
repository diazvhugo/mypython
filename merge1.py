
import itertools

a = ['1','2','3']
b = ['4','5','6','7']

print list(itertools.chain(*zip(a, b)))
print a+b
