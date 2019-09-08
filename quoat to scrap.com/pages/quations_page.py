from bs4 import BeautifulSoup
from locator.quations_page_locator import QuotesPageLocator
from passer.quotes import QuoteParser

class QuotesPages:
    def __init__(self, page):
        self.page = page
        self.soup = BeautifulSoup(self.page , 'html.parser')

    @property
    def quote(self):
        locator = QuotesPageLocator.QUOTES
        quotes_tags = self.soup.select(locator)
        return [QuoteParser(e) for e in quotes_tags]


