import csv

with open('test.csv', "rb") as ifile, open('ttest.csv', "wb") as ofile:
    reader = csv.reader(ifile)
    writer = csv.writer(ofile, delimiter='', quotechar='"', quoting=csv.QUOTE_ALL)

for row in reader:
    writer.writerow(row)


