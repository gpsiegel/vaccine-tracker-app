import csv

#final = []

with open('us_vaccine.csv', 'r') as fi:
    reader = csv.reader(fi, delimiter=',')
    rows = list(reader)

latest = rows[-1]

latest_trim = ['Date: '+ latest[1], \
    'Vaccine type: '+ latest[2], \
    'total vaccinations: '+ latest[4], \
    'people vaccinated: '+ latest[5], \
    'total vaccinated: '+ latest[6]]
    
for lt in latest_trim:
    print(lt)