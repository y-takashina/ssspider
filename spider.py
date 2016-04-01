import re
import time
import requests
from bs4 import BeautifulSoup

pattern = re.compile(r'(\S+?)「(.*?)」', re.DOTALL)

file = open(r".\archive\archive.txt")
urls = file.readlines()
file.close()

for url in urls:
    file = open(".\\log\\" + url[-12:-6] + ".log", 'w')
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "lxml")
    article = soup.find('div', attrs={"class": "article-body-more"})
    talks = pattern.findall(article.text)
    for talk in talks:
        teller = talk[0]
        words = re.sub("<br />|(&nbsp;)|　|\s", "", talk[1])
        print(teller + ',' + words)
        line = teller + ',' + words + '\n'
        file.write(line)
    file.close()
    time.sleep(5)




