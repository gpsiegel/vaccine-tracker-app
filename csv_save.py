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
    
    latest_trim = [latest[1], latest[2], latest[4], latest[5], latest[6]]
    
    with open("us_vaxx.csv", "w") as fo:
        writer = csv.writer(fo, delimiter=',')
        writer.writerow(latest_trim)

def main():
    csv_create()
    csv_sort()

if __name__ == "__main__":
    main()
