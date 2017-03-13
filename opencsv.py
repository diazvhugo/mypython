
import csv

file1='data1.csv'
file2='data2.csv'

with open(file1) as f:
    records = csv.DictReader(f)
    for row in records:
         print row.pop("Nombre")

with open(file2) as f:
    records = csv.DictReader(f)
    for row in records:
         print row.pop(" edad")

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
for i, j in zip(first_dict, second_dict):
   print i + " / " + second_dict[j]
   third_dict[i] = second_dict[j]
print third_dict

with open('out.csv', 'wb') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in third_dict.items():
       writer.writerow([key, value])
