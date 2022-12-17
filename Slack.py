import csv
import requests as r
from bs4 import BeautifulSoup # library to parse HTML documents

wiki_page_request = r.get("https://en.wikipedia.org/wiki/List_of_prime_ministers_of_Egypt")
wiki_page_text = wiki_page_request.text
soup = BeautifulSoup(wiki_page_text, 'html.parser')
right_table=soup.find('table', {'class':'wikitable'})
headers = []
for i in right_table.find_all('th'):
 title = i.text
 headers.append(title)
 if title==('Political party\n'):
     break
headers.insert(3,'Took office\n')
headers.insert(4,'left office\n')
headers.pop(0)
headers[0]=headers[0].replace('Portrait','Table content')
rows = []

# Find all `tr` tags
data_rows = right_table.find_all('tr')

for row in data_rows:
    value = row.find_all('td')
    beautified_value = [ele.text.strip() for ele in value]
    # Remove data arrays that are empty
    if len(beautified_value) == 0 or (str(beautified_value).__contains__('Egypt')) or (str(beautified_value).__contains__(' United Arab Republic')):
        continue
    rows.append(beautified_value)

print(headers)
for i in range(len(rows)):
    for j in range(len(rows[i])):
       print(rows[i][j])

with open('book1.csv', 'w',newline= "",encoding="UTF-8" ) as output:
    writer = csv.writer(output)
    writer.writerow(headers)
    writer.writerows(rows)
