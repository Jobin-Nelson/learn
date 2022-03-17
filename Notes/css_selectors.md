# CSS Selectors
- It is a way of selecting specific information using css
- You can play with CSS selectors [here](https://try.jsoup.org)

## Navigation
- Console
	- `$$('h1')`          -> for CSS selectors
	- `$x('h1')`          -> for XPath
	- `$$('.heading')`    -> tags with class heading
	- `$$('.heading')[2]` -> second tag with class heading
- Elements
	- `h1`                      -> all h1 tags
	- `h1.heading`              -> h1 tag with heading class
	- `.heading`                -> all elements with class heading
	- `#plus`                   -> all elements with id plus
	- `[style="color: black;"]` -> elements with this attribute
	- `[data-country]`          -> all elements with attribute name data-country
	- `[href^="tel"]`           -> all elements with href attribute beginning with tel
	- `[href$="2"]`             -> all elements with href attribute ending with 2
	- `[href*="ca"]`            -> all elements which contains ca as href attribute
	- `div > p`                 -> p tag that is a direct child of div
	- `div p`                   -> all p tags inside div
	- `div + p`                 -> p tag that is an immediate siblings of div
	- `div ~ p`                 -> all p tags that are siblings of div
	- `td:nth-child(2)`         -> all td tags that are the second child of its parent
	- `td:last-child`           -> last td tag of each parent having td tags
