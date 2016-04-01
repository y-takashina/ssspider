import re
import requests
from bs4 import BeautifulSoup

archive = requests.get("http://minnanohimatubushi.2chblog.jp/archives/2015-08.html")
soup = BeautifulSoup(archive.text, "lxml")

for month in soup.find('div', attrs={"class":"plugin-monthly sidewrapper"}).findAll('option'):
    print(month['value'])


