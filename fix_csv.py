import csv

flag = True
with open('data/sample.csv', 'rt',encoding="utf-8", errors='ignore') as ifile, open('data/fixed.csv', 'wt',newline='',encoding="utf-8") as ofile:
    reader = csv.reader(ifile, delimiter=',')
    writer = csv.writer(ofile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

    for row in reader:
        if flag:
            flag=False
            continue

        able = True
        if len(row) != 14:
            able = False
        for coll in row:
            if not coll:
                able = False
        if able:
            writer.writerow(row)