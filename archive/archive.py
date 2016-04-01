import re
import requests
from bs4 import BeautifulSoup

res = requests.get("http://minnanohimatubushi.2chblog.jp/")
soup = BeautifulSoup(res.text, "lxml")
monthly_pages = []

for month in soup.find('div', attrs={"class": "plugin-monthly sidewrapper"}).findAll('option'):
    if month['value']:
        monthly_pages.append(month['value'])

archive = []

for month in monthly_pages:
    page = requests.get(month)
    soup = BeautifulSoup(page.text, "lxml")
    for bookmark in soup.findAll('a', attrs={"rel": "bookmark"}):
        archive.append(bookmark['href'])
        print(bookmark['href'])

# print(archive)


