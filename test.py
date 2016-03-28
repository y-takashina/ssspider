import sys
import json
import requests
from bs4 import BeautifulSoup

res = requests.get("http://minnanohimatubushi.2chblog.jp/archives/1953343.html")
soup = BeautifulSoup(res.text.encode(res.encoding), "lxml")

print(soup.title)

# file = open('.log', 'w')
# file.writelines(soup.title)
# file.close()





