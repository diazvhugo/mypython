
import csv
#from collections import defaultdict

file1='data1.csv'
file2='data2.csv'
#fieldnames = {"Nombre"}
#result = defaultdict(dict)

#f = open(file1, 'rb')
#reader = csv.reader(f)
#for row in reader:
#    print row
#f.close()

with open(file1) as f:
    records = csv.DictReader(f)
    for row in records:
         print row

with open(file2) as f:
    records = csv.DictReader(f)
    for row in records:
         print row

#for csvfile in (file1, file2):
#    with open(csvfile) as infile:
#        reader = csv.DictReader(infile)
#        for row in reader:
#            id = row.pop("Nombre")
#            for key in row:
#                fieldnames.add(key) # wasteful, but I don't care enough
#                result[id][key] = row[key]

#print result

#with open("out.csv", "w") as outfile:
#    writer = csv.DictWriter(outfile, sorted(fieldnames))
#    writer.writeheader()
#    for item in result:
#        result[item]["Nombre"] = item
#        writer.writerow(result[item])

first_dict = {}
with open(file1, 'r') as f:
    csvReader = csv.reader(f)
    next(csvReader, None) # skip the header
    for row in csvReader:
        key = row[0]
        first_dict[key] = row[1]
# Second dictionary
second_dict = {}
with open(file2, 'r') as f:
    csvReader = csv.reader(f)
    next(csvReader, None) # skip the header
    for row in csvReader:
        key = row[0]
        second_dict[key] = row[1]

print first_dict
print second_dict

for x in first_dict:
	print (x)
for x in second_dict:
	print second_dict.get(x)

third_dict = {}
for x in first_dict:
	for y in second_dict:
		third_dict[x] = second_dict.get(y)

for i, j in zip(first_dict, second_dict):
   print i + " / " + second_dict[j]
   third_dict[i] = second_dict[j]
print third_dict
