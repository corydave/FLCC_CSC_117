import requests
from bs4 import BeautifulSoup

page = requests.get('https://phishingdemo.org/python/scraping/4070ti.html', headers={"User-Agent": ""})
print(page.status_code)
# print(page.text)

soup = BeautifulSoup(page.content, 'html.parser')
# print(soup)

# classes = soup.find_all(class_="description")
# print(classes[1])

quantity = soup.find(id="remaining").string
print(quantity)
