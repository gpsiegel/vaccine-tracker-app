import csv

#final = []

with open('us_vaccine.csv', 'r') as fi:
    reader = csv.reader(fi, delimiter=',')
    rows = list(reader)

latest = rows[-1]
for l in latest:
    print(l)