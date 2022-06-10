import requests
from bs4 import BeautifulSoup

URL = "https://learnershare.com/sitemap_index.xml"
page = requests.get(URL)
ls_main = BeautifulSoup(page.content, "lxml")
# print(posh_main.prettify())
table1 = ls_main.find('sitemapindex')
# print(table1.prettify())
all_links = []
for i in table1.find_all('loc'):
    title = i.text
    all_links.append(title)
# print(all_links)
with open("mainlsp.txt", "w+") as txt_file:
    for i in all_links:
        txt_file.write(i +"\n")

