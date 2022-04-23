# Regular Expression
- Used to find matching patterns in a corpus

# Syntax
- `verbatim text`
	- verbatim text is matched literally
- `.`
	- Any one character
- `\`
	- escape character
	- most cases, treat the character after it as a literal character `\.` is `.`
- `^` and `$`
	- anchors
	- `^` matches the beginning of the line
	- `$` matches the end of the line
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
	- or, match one thing or the other
- `(abc)`
	- groups common characters
- `\s`,`\S`
	- `\s` any whitespace character
	- `\S` any non-whitespace character

- Examples
	- `https\?://\S*\.[A-Za-z]\+\S` -> for extracting only web links
