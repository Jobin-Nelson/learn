# XPath
- XML Path was introduced to find information from XML
- You can play with xpath [here](https://scrapinghub.github.io/xpath-playground/)

## Navigation
- `/`                             -> root element
- `/html`                         -> children of html
- `//`                            -> descendants
- `/..`                           -> parent
- `//a/@href`                     -> attribute
- `//a/text()`                    -> text
- `//a[2]`                        -> 2nd `a` tag, indexing begins at 1
- `//a[@id="first"]`              -> `a` tag with attribute id="first"
- `//a[contains(text(),"Hello")]` -> `a` tag that contains the specified value
- `//h2/descendant::*`            -> all the descendants
- `//*[@class="anchor"]`          -> any tag with the class anchor
- `//a[last()]`                   -> last `a` tag
- `//a[@data-quantity>3]`         -> all `a` tag with attribute data quantity > 3
- `//a[@id="first" and @class="blue"]`    -> `a` tag that satisfies both condition, `or` also works
- `//a[@id="first"]/following-sibling::p` -> `p` tag that is a sibling of `a` tag with id first
- `normalize-space(//a[@id="first"])`     ->  cleans up new line, space
