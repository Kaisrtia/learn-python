file1 = open("../data/data.txt", "a+")
file1.seek(0)

for line in file1:
  print(line.strip())

import csv 

file2 = open("../data/data.csv", "a+")
file2.seek(0)
csv_reader2 = csv.DictReader(file2)
print(csv_reader2.fieldnames)