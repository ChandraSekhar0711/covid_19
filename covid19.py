import requests 
from bs4 import BeautifulSoup 
from texttable import Texttable
  

url = 'https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/'
  
 
page = requests.get(url) 
soup = BeautifulSoup(page.text, 'html.parser') 

data = [] 
  
 
data_iterator = iter(soup.find_all('td')) 

   
while True: 
    try: 
        country = next(data_iterator).text 
        confirmed = next(data_iterator).text 
        deaths = next(data_iterator).text 
        continent = next(data_iterator).text 
  
        
        s=confirmed.replace(', ', '')
        k=deaths.replace(', ', '')
        data.append(( country, s, k, continent )) 
  
    
    except StopIteration: 
        break
  


table =Texttable() 
table.add_rows([(None, None, None, None)] + data) 
table.set_cols_align(('c', 'c', 'c', 'c'))  
table.header((' Country ', ' Number of cases ', ' Deaths ', ' Continent ')) 
  
print(table.draw()) 
