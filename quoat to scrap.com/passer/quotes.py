from locator.quote_locator import QuotesLocator


class QuoteParser:
    def __init__(self, element):
        self.element = element

    def __repr__(self):
        return f"""Author:{self.author}
Quote:{self.content}
                 """

    @property
    def content(self):
        locator = QuotesLocator.QUOTE
        return self.element.select_one(locator).string

    @property
    def author(self):
        locator = QuotesLocator.AUTHOR
        return self.element.select_one(locator).string
    
    @property
    def tags(self):
        locator = QuotesLocator.TAGS
        return [e.string for e in self.element.select(locator)]