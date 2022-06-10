import urllib.request
from pprint import pprint
from html_table_parser.parser import HTMLTableParser
import pandas as pd

def url_get_contents(url):

	#making request to the website
	req = urllib.request.Request(url=url)
	f = urllib.request.urlopen(req)

	return f.read()

xhtml = url_get_contents('https://www.moneycontrol.com/india\
/stockpricequote/refineries/relianceindustries/RI').decode('utf-8')

# Defining the HTMLTableParser object
p = HTMLTableParser()
p.feed(xhtml)
pprint(p.tables[1])
print("\n\nPANDAS DATAFRAME\n")
print(pd.DataFrame(p.tables[1]))
