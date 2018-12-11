import csv

flag = True
with open('data/sample.csv', 'rt',encoding="utf-8", errors='ignore') as ifile, open('data/fixed.csv', 'wt',encoding="utf-8") as ofile:
    reader = csv.reader(ifile, delimiter=',')
    writer = csv.writer(ofile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

    for row in reader:
        if flag:
            flag=False
            continue
        print(row)
        if len(row) != 14:
            continue
        for coll in row:
            if coll == "":
                continue
        writer.writerow(row)