import csv
import fileinput

flag = True
counter = 0;
with open('data/oddetect.csv', 'rb') as ifile, open('data/fixed.csv', 'wb') as ofile:
    reader = csv.reader(ifile, delimiter=',')
    writer = csv.writer(ofile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    for line in ifile:
        process(line)
    for row in reader:
        if (flag):
            flag = False
            continue
        counter +=1
        print(row)