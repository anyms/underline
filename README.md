## Underline

A human friendly web crawling library

```python
from underline import Underline


_ = Underline(url="https://duckduckgo.com")
page = {
    "title": _.title(),
    "slogan": _.css(".badge-link__title").text(),
    "images": _.images()
}
```

### Methods

- **.css(selector)** - select elements with given css selector
- **.text(s=None)** - get or set text of html element(s)
- **.html(s=None)** - get or set html string of html element(s)
- **.map(expr)** - map selected elements
- **.also(expr)** - filter selected element with given expression (lambda or function)
- **.children()** - get children of selected elements
- **.text_nodes()** - get text nodes of selected elements
- **.extend(Selector|list)** - add new html elements
- **.append(Selector|HTMLElement)** - append given element to selected elements
- **.prepend(Selector|HTMLElement)** - prepend given element to selected elements
- **.remove()** - remove selected elements from document
- **.each(expr)** - loop through each element
- **.siblings()** - get all sibling elements
- **.parents()** - get all parents of selected elements
- **.remove_attr(name)** - remove attribute from selected elements
- **.remove_class(name)** - remove class names from selected elements
- **.add_class(name)** - add class to selected elements
- **.filter(selector)** - filter selected elements with css selector
- **.src()** - get element src attribute
- **.href()** - get element href attribute
- **.action()** - get element action attribute
- **.attr(key, value=None)** - set or get element(s) attribute(s)
- **.size()** - get selected elements size
- **.val()** - get value of form element
- **.parent()** - get parent of selected element
- **.last()** - get last element from selected elements
- **.first()** - get first element from selected elements
- **.get(index)** - get element by index
- **.audios()** - get audio element sources from selected elements
- **.videos()** - get video element sources from selected elements
- **.images()** - get image element sources from selected elements
- **.title()** - get website title
- **.clean()** - remove duplicates


### Example 1: Extracting Links


```python
_ = Underline(url="https://github.com/lineofapi/lineofjs-dom")
targets = _.css("ul li a").also(lambda el: el.href().startswith("#")).map(lambda el: el.href())
print(targets)
```

Output:

```
Selector { #dom-method-$, #dom-method-action, #dom-method-addClass, #dom-method-append, #dom-method-attr, #dom-method-bind, #dom-method-children, #dom-method-click, #dom-method-css, #dom-method-disable, #dom-method-enable, #dom-method-extend, #dom-method-each, #dom-method-filter, #dom-method-first, #dom-method-get, #dom-method-hide, #dom-method-height, #dom-method-href, #dom-method-html, #dom-method-isDisabled, #dom-method-innerHeight, #dom-method-innerWidth, #dom-method-last, #dom-method-offset, #dom-method-on, #dom-method-parent, #dom-method-parents, #dom-method-prepend, #dom-method-ready, #dom-method-removeClass, #dom-method-remove, #dom-method-removeAttr, #dom-method-show, #dom-method-siblings, #dom-method-src, #dom-method-toggleClass, #dom-method-text, #dom-method-unbind, #dom-method-val, #dom-method-width }
```
