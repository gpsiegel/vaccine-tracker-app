import requests
import csv

csv_file = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/country_data/United%20States.csv'

req = requests.get(csv_file)
saved_content = req.content 
csv_saved = open('us_vaccine.csv', 'wb')

csv_saved.write(saved_content)
csv_saved.close()