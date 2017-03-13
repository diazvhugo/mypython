#!/usr/bin/python
import re
import datetime
import csv
from collections import Counter

file = '/var/log/syslog'
regexp = '^([a-zA-Z]+\s?\d+\s?\d+\:\d+\:\d+).*'

lines = []
	
for line in open(file):
	match = re.search(regexp, line)
	print "%s" % (match.group(1))
	lines.append(match.group(1))

print lines.count("Mar 13 03:26:25")
c = Counter(lines)
print c.items()
#Extract Date
dt_obj = datetime.datetime.strptime(lines[1], "%b %d %H:%M:%S")
print dt_obj
print "minuto: " + repr(dt_obj.minute) +" " + "dia:" + repr(dt_obj.day)

#Write CSV
with open('/home/hugo/Test/test.csv', 'wb') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(('Date', 'Time'))
    wr.writerow(lines)

#Reverse Sort the dates
#lines.sort(key=lambda x: time.strptime(x,'%b %d %H:%M:%S'), reverse=True)
#for n in range  (1,100):
#	print "SFecha: %s" % lines[n]

#echo "ocurencias Fecha";awk '{print $1, $2, $3}' /var/log/syslog | uniq -c | sort -nr
