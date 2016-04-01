import sys
import json
import re
import requests
from bs4 import BeautifulSoup

res = requests.get("http://minnanohimatubushi.2chblog.jp/archives/1953343.html")
# soup = BeautifulSoup(res.text.encode(res.encoding), "lxml")
soup = BeautifulSoup(res.text, "lxml")

for article in soup.findAll('div', attrs={"class": "t_b"}):
    for br in article.findAll('br'):
        next1 = br.nextSibling
        if not next1 or next1.name == 'br':
            continue
        next2 = next1.nextSibling
        if next2 and next2.name == 'br':
            text = str(next1).strip()
            if text:
                print(text)

# print(soup("div", attrs={"class": "t_b"}))

# print(soup.title.string)

# file = open('.log', 'w')
# file.writelines(soup.title)
# file.close()





