import requests
from bs4 import BeautifulSoup
from texttable import Texttable
import csv

url = 'https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/'

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
#print(soup)   #displays whole html code ....
data = []

data_iterator = iter(soup.find_all('td'))




while True:
    try:
        country = next(data_iterator).text
        confirmed = next(data_iterator).text
        deaths = next(data_iterator).text
        continent = next(data_iterator).text

        s = confirmed.replace(', ', '')
        k = deaths.replace(', ', '')
        data.append([country, s, k,continent])

    except StopIteration:
        break

table = Texttable()
table.add_rows([(None, None, None,None )] + data)
table.set_cols_align(('c', 'c', 'c', 'c' ))  # 'l' denotes left, 'c' denotes center, and 'r' denotes right 
table.header((' Country ', ' Number of cases ', ' Deaths ', 'continent'))
print(table.draw())

with open("covid.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)

