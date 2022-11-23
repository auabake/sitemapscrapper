import requests
from bs4 import BeautifulSoup

# def get_allpost_sitemaps(ls):

#     URL = "https://learnershare.com/sitemap_index.xml"
#     page = requests.get(URL)
#     ls_main = BeautifulSoup(page.content, "lxml")
#     table1 = ls_main.find('sitemapindex')
#     all_links = []
#     for i in table1.find_all('loc'):
#         title = i.text
#         all_links.append(title)
#     post_links = all_links[0:250]
#     print(post_links)

URL = "https://learnershare.com/sitemap_index.xml"
page = requests.get(URL)
ls_main = BeautifulSoup(page.content, "lxml")
main_sitemap = ls_main.find('sitemapindex')
all_links = []
for i in main_sitemap.find_all('loc'):
    link = i.text
    all_links.append(link)
post_links = all_links[0:2]
# print(post_links)


all_data = []
for url in post_links:
    print(url)
    req = requests.get(url)
    jrpage = BeautifulSoup(req.content, "lxml")
    jrsitemap = jrpage.find('urlset')
    jrlinks = []
    for x in jrsitemap.find_all('loc'):
        jrlink = x.text
        jrlinks.append(jrlink)
    all_data.extend(jrlinks)
# print (all_data)
with open("alldatatest.txt", "w+") as txt_file:
    for k in all_data:
        txt_file.write(k +"\n")