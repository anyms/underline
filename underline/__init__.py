import requests
from bs4 import BeautifulSoup

from .core.selector import Selector


class Underline(Selector):
    def __init__(self, html=None, url=None, method="get", **kwargs):
        self.session = requests.Session()
        if html is None:
            resp = self.session.request(url=url, method=method, **kwargs)
            self.content = resp.text
            self.url = resp.url
            self.document = BeautifulSoup(resp.content, "html.parser")
            Selector.__init__(self, document=self.document, elements=[], url=url)
        else:
            self.document = BeautifulSoup(html, "html.parser")
            self.content = html
            self.url = url
            Selector.__init__(self, document=self.document, elements=[], url=url)
    
    def __repr__(self):
        return str(self)
    
    def __str__(self):
        return str(self.document)

    def title(self):
        return self.document.title.text

    def follow(self, url, method="get", **kwargs):
        resp = self.session.request(url=url, method=method, **kwargs)
        self.url = resp.url
        self.content = resp.text
        self.document = BeautifulSoup(resp.content, "html.parser")

