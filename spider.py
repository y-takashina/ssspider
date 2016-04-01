import re
import requests
from bs4 import BeautifulSoup



bookmarks = []
archive = requests.get("http://minnanohimatubushi.2chblog.jp/archives/2015-08.html")
archive_soup = BeautifulSoup(archive.text, "lxml")
for bookmark in archive_soup.findAll('a', attrs={"rel": "bookmark"}):
    bookmarks.append(bookmark['href'])

print(bookmarks)



# pattern = re.compile(r"(.+)「(.*)」", re.DOTALL)
# res = requests.get("http://minnanohimatubushi.2chblog.jp/archives/1953343.html")
# soup = BeautifulSoup(res.text, "lxml")
#
# for article in soup.findAll('div', attrs={"class": "t_b"}):
#     for br in article.findAll('br'):
#         next1 = br.nextSibling
#         if not next1 or next1.name == 'br':
#             continue
#         next2 = next1.nextSibling
#         if next2 and next2.name == 'br':
#             matched = pattern.match(next1)
#             if matched:
#                 print(matched.group(1).strip() + "," + matched.group(2))

# file = open('.\log\1.log', 'w')
# file.writelines()
# file.close()




