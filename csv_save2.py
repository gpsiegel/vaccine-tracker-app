import csv
import requests

def csv_create():
    csv_file = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/country_data/United%20States.csv'

    req = requests.get(csv_file)
    saved_content = req.content 
    csv_saved = open('us_vaccine.csv', 'wb')

    csv_saved.write(saved_content)
    csv_saved.close()

def csv_sort():
    with open('us_vaccine.csv', 'r') as fi:
        reader = csv.reader(fi, delimiter=',')
        rows = list(reader)

    latest = rows[-1]
    
    trim = ['Vaccine Type: '+ latest[2], \
        'Total Vaccinations: '+ latest[4], \
        'People Vaccinated: '+ latest[5], \
        'Total Vaccinated: '+ latest[6]]

    with open("us_vaxx.csv", "w") as fo:
        writer = csv.writer(fo, delimiter='\n')
        writer.writerow(trim)

def main():
    csv_create()
    csv_sort()

if __name__ == "__main__":
    main()
