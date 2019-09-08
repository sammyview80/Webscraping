import requests
from pages.quations_page import QuotesPages
page = requests.get('http://quotes.toscrape.com').content
page_html = QuotesPages(page)

for page in page_html.quote:
    print(page)