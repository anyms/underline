import requests
from bs4 import BeautifulSoup

from .core.selector import Selector


class Underline(Selector):
    def __init__(self, html=None, url=None):
        if html is None:
            resp = requests.get(url)
            self.content = resp.text
            self.url = resp.url
            self.document = BeautifulSoup(resp.content, "html.parser")
            Selector.__init__(self, document=self.document, elements=[], url=html)
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


# s = """
# <div>
#     <button>Click me! <span>test</span> </button>
#     <div class="red green">I am Red</div>
#     <ul>
#         <li>Item 1</li>
#         <li>Item 2</li>
#         <li>Item 3</li>
#         <li>Item 4</li>
#         hi
#         <br/>
#         hello
#     </ul>
#     <audio src="/play.mp3"/>
#     <img src="/hello.jpg"/>
#     <img src="./hello2.jpg"/>
#     <a href="#">Link</a>

#     <form method="post" action="/process.php">
#         <input type="text" name="username"/>
#         <input type="password" name="password"/>
#         <input type="submit" name="submit" value="Login"/>
#     </form>
# </div>
# """


# _ = Underline(url="https://github.com/lineofapi/lineofjs-dom")
# output = _.css("ul li a").also(lambda el: el.href().startswith("#")).map(lambda el: el.href())
# print(output)
