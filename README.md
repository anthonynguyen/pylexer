# pylexer
### A tiny lexer module written in Python


## About
**By Anthony Nguyen**

I was learning about string tokenization for NLP and I wrote this as a sort of application about the concepts I'm learning.

It *will* stop if it does not find a token at the beginning of the data it is looking at.

## Usage
	import pylexer, re
	lexer = pylexer.Lexer([
		("word", "[a-z]+"),
		("shortdate", "\d{1,2}\/\d{1,2}\/\d{4}")
		], re.I)
	for token in lexer.scan("I was born on 01/01/1970", True):
		print token

`Lexer.__init__` takes two arguments: a list of tokens as tuples `("name", "regex")`, and any regex flags
`Lexer.addTokens` takes a list of tokens as tuples `("name", "regex")`
`Lexer.addFlags` takes any number of regex flags
`Lexer.scan` is an iterator and takes two arguments: the string to scan, and whether or not to ignore whitespace (optional, disabled by default). It returns objects of the `Token` class.

The `Token` class is basically a variable container. It holds the following information:

* `name` - The token's name
* `rule` - The regex used to match the token
* `data` - The token's matched data
* `start` - The start index (in the original string) of the token's data
* `end` - The end index (in the original string) of the token's data

The `Scanner` class is the class that's doing the actual scanning work, but it should only ever need to be used from the `Lexer` class.

## License
MIT licensed. See LICENSE.