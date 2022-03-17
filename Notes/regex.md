# Regular Expression
- Used to find matching patterns in a corpus

# Syntax
- `verbatim text`
	- verbatim text is matched literally
- `.`
	- single character wildcard
- `\`
	- escape character
	- most cases, treat the character after it as a literal character `\.` is `.`
- `^` and `$`
	- anchors
	- `^` matches the beginning of the string
	- `$` matches the end of the string
- `*`, `+`, `?`
	- `*` matches 0 to many of the previous character
	- `+` matches 1 to many of the previous character
	- `?` matches 0 or 1 of the prevous character
- `{n}` and `{n,m}`
	- `{n}` matches exactly n times of the previous character
	- `{n,m}` matches to a range between n...m inclusively of the previous character
- `[abc]` and `[a-z]`
	- `[abc]` matches a single character that is either `a`, `b` or `c`
	- `[a-z]` matches any character between a...z inclusively
- `|`
	- exclusive or, match one thing or the other
- `(abc)`
	- groups common characters
