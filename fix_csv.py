import csv
with open('data/oddetect.csv', 'rb') as ifile, open('data/fixed.csv', 'wb') as ofile:
    csv_reader = csv.reader(ifile, delimiter=',')
    reader = csv.reader(ifile)
    writer = csv.writer(ofile, delimiter='', quotechar='"', quoting=csv.QUOTE_ALL)
    for row in reader:
        writer.writerow(row)