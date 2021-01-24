from urllib.parse import urljoin
from bs4.element import ResultSet
from bs4 import BeautifulSoup

from ..utils import colors


class Selector(list):
    def __init__(self, document, elements=[], url=None):
        self.url = url
        self.document = document
        
        self.extend(elements)

        self.size    = lambda: len(self)
        self.val     = lambda: self[0].get("value")
        self.parent  = lambda: self.new(self[0].parent)
        self.last    = lambda: self.new(self[-1])
        self.first   = lambda: self.new(self[0])
        self.get     = lambda index: self.new(self[index])
        self.new     = lambda els: Selector(self.document, els, self.url)
        self.audios  = lambda: self._find_src_attrs("audio")
        self.videos  = lambda: self._find_src_attrs("video")
        self.images  = lambda: self._find_src_attrs("img")
        self.to_set  = lambda: self.new(list(set(self)))


    def __repr__(self):
        return str(self)
    
    def __str__(self):
        s = "{}Selector {{ {}".format(colors.GREEN, colors.END)
        for el in self:
            s += "{}, ".format(el)
        if len(self) > 0:
            s = s[:-2]
        s = "{}{} }}{}".format(s, colors.GREEN, colors.END)
        return s

    def text(self, s=None):
        if s is None:
            return self[0].text
        
        for el in self:
            el.string = s
        return self

    def html(self, s=None):
        if s is None:
            return "".join([str(x) for x in self[0].contents])
        
        for el in self:
            tmp = BeautifulSoup(s, "html.parser")
            el.string = ""
            el.append(tmp)
        return self

    def map(self, expr):
        els = []
        for el in self:
            els.append(expr(self.new(el)))
        return self.new(els)

    
    def also(self, expr):
        els = []
        for el in self:
            if type(el) is not Selector:
                el = self.new(el)
            if expr(el):
                els.append(self.new(el))
        return self.new(els)

    def css(self, selector):
        out = []
        if self.size() == 0:
            els = self.document.select(selector)
        else:
            els = self[0].select(selector)
        for el in els:
            out.append(el)
        return self.new(els)

    def children(self):
        els = []
        for child in self[0].findChildren(recursive=False):
            els.append(child)

        return self.new(els)

    def text_nodes(self):
        els = []
        for child in self[0].findChildren(recursive=False, text=True):
            if child != "\n":
                els.append(child.strip())

        return self.new(els)

    def extend(self, node):
        if type(node) is list or type(node) is Selector or type(node) is ResultSet:
            for n in node:
                super(Selector, self).append(n)
        else:
            super(Selector, self).append(node)
        return self
    
    def append(self, node):
        if type(node) is list or type(node) is Selector or type(node) is ResultSet:
            for n in node:
                for el in self:
                    el.append(n)
        else:
            for el in self:
                el.append(node)
        return self

    def prepend(self, node):
        if type(node) is list or type(node) is Selector or type(node) is ResultSet:
            for n in node:
                for el in self:
                    el.insert(0, n)
        else:
            for el in self:
                el.inset(0, node)
        return self

    def remove(self):
        for el in self:
            el.decompose()
            super(Selector, self).remove(el)
        return self

    def each(self, expr):
        for el in self:
            expr(self.new(el))
        return self

    def siblings(self):
        parent = self[0].parent
        els = []
        for el in parent.findChildren(recursive=False):
            if el != self[0]:
                els.append(el)
        return self.new(els)

    def parents(self):
        els = []
        for el in self:
            if el.parent not in els:
                els.append(el.parent)
        return self.new(els)


    def remove_attr(self, name):
        for el in self:
            el.attrs.pop(name)
        return self

    def remove_class(self, name):
        cs = name.split(" ")
        for c in cs:
            for el in self:
                try:
                    el["class"].pop(el["class"].index(c))
                except ValueError:
                    pass
        return self

    def add_class(self, name):
        cs = name.split(" ")
        for c in cs:
            for el in self:
                try:
                    el["class"].append(c)
                except ValueError:
                    pass
        return self

    def filter(self, selector):
        els = []
        for el in self:
            s = "<div>{}</div>".format(el)
            soup = BeautifulSoup(s, "html.parser").findChildren(recursive=False)[0]
            if len(soup.findChildren(selector, recursive=False)) > 0:
                els.append(el)
        return self.new(els)

    def src(self):
        try:
            if self[0].has_attr("src"):
                src = self[0]["src"].strip()
            else:
                src = self[0].find("source")["src"]
        except TypeError:
            return None

        if not src.startswith("http://") or not src.startswith("https://") and self.url is not None:
            return urljoin(self.url, src)
        return src

    def href(self):
        if self[0].has_attr("href"):
            href = self[0]["href"].strip()

            if not href.startswith("http://") or not href.startswith("https://") and self.url is not None:
                return urljoin(self.url, href)
            return href
        
        return None

    def action(self):
        if self[0].has_attr("action"):
            action = self[0]["action"].strip()

            if not action.startswith("http://") or not action.startswith("https://") and self.url is not None:
                return urljoin(self.url, action)
            return action
        
        return None

    def _find_src_attrs(self, tag):
        out = []

        if len(self) == 0:
            sels = self.document.select(tag)
        else:
            sels = self[0].select(tag)

        for sel in sels:
            if sel.has_attr("src"):
                src = sel["src"].strip()
            else:
                src = sel.find("source")["src"]
            if src == "#" and src == "":
                continue
            if not src.startswith("http://") or not src.startswith("https://"):
                if self.url is not None:
                    out.append(urljoin(self.url, src))
                else:
                    out.append(src)
            else:
                out.append(src)

        return out

    def attr(self, key, value=None):
        if value is None:
            return self[0][key]
        
        for el in self:
            el[key] = value
        return self