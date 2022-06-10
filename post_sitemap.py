import requests
from bs4 import BeautifulSoup

URL = "https://learnershare.com/post-sitemap.xml"
page = requests.get(URL)
posh_main = BeautifulSoup(page.content, "lxml")
# print(posh_main.prettify())
table1 = posh_main.find('urlset')
# print(table1.prettify())
all_links = []
for i in table1.find_all('loc'):
    title = i.text
    all_links.append(title)
# print(all_links)
# with open("lsp1.txt", "w+") as txt_file:
#     for i in all_links:
#         txt_file.write(i +"\n")
new_links = all_links
if len(new_links) == len(set(new_links)):
    print('no duplicates')
else:
     print('you have duplicates')