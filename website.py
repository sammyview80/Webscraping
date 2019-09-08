import requests
from bs4 import BeautifulSoup

page = requests.get('http://example.com')
page_html = page.content
soup = BeautifulSoup(page_html, 'html.parser')
page_preetify = soup.prettify()
title = soup.find('h1').string
print(title)