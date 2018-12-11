import csv

def fix_csv_file(file_name):
    flag = True
    with open(file_name, 'rt',encoding="utf-8", errors='ignore') as ifile, open('data/fixed.csv', 'wt',newline='',encoding="utf-8") as ofile:
        reader = csv.reader(ifile, delimiter=',')
        writer = csv.writer(ofile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

        count_wrong = 0
        count_right = 0
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
                count_right += 1
                writer.writerow(row)
            else:
                count_wrong += 1

    return (count_wrong, count_right)



print(fix_csv_file('data/oddetect.csv'))