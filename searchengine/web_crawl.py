import requests
import csv
from bs4 import BeautifulSoup


URL = "https://saravanaseeker.wordpress.com/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
# geting all value
find_value = soup.find("a", target='_self')

title = find_value.text
links = soup.find_all("a")

payload = []
for link in links:
    data = {}
    data['title'] = link.text.strip()
    data['url'] = link["href"]
    payload.append(data)
print(payload)

filename = 'saravanaseeker.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f, ['title', 'url'])
    w.writeheader()
    for data in payload:
        w.writerow(data)
