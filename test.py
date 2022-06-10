import urllib.request
from pprint import pprint
from html_table_parser.parser import HTMLTableParser


def url_get_contents(url):
    req = urllib.request.Request(url=url)
    f = urllib.request.urlopen(req)
    return f.read()


def main():
    url = 'https://poshuae.com/sitemap_index.xml'
    xhtml = url_get_contents(url).decode('utf-8')

    p = HTMLTableParser()
    p.feed(xhtml)
    pprint(p.tables)


if __name__ == '__main__':
    main()