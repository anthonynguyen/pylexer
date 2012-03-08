# A lexer in Python
# By Anthony Nguyen
# MIT Licensed
#
# Pretty basic; easily extensible

import re

class Token():
	def __init__(self, name, rule, data, start, end):
		self.name = name
		self.rule = rule
		self.data = data
		self.start = start
		self.end = end

	def __str__(self):
		return "{0}({1}): {2}".format(self.name, self.rule, self.data)

class Scanner():
	def __init__(self, data, tokens, flags, ignoreWhitespace):
		self.data = data
		self.tokens = tokens
		r = []
		for name in tokens:
			r.append("(?P<{0}>{1})".format(name, tokens[name]))
		self.regex = re.compile("|".join(r), *flags)
		self.ignoreWhitespace = ignoreWhitespace
		self.whitespace = re.compile("\s*", re.MULTILINE)
		self.position = 0

	def __iter__(self):
		return self

	def next(self):
		if self.ignoreWhitespace:
			whitespace = self.whitespace.match(self.data, pos = self.position)
			if whitespace is not None:
				self.position = whitespace.end()
		match = self.regex.match(self.data, pos = self.position)
		if match is not None:
			self.position = match.end()
			return Token(match.lastgroup, self.tokens[match.lastgroup], match.group(match.lastgroup), match.start(), match.end())
		else:
			raise StopIteration

class Lexer():
	tokens = {}
	def __init__(self, tokens, *flags):
		for name, rule in tokens:
			self.tokens[name] = rule
		self.flags = list(flags)

	def addTokens(self, tokens):
		for name, rule in tokens:
			self.tokens[name] = rule

	def addFlags(self, *flags):
		self.flags += list(flags)

	def scan(self, data, ignoreWhitespace = False):
		return Scanner(data, self.tokens, self.flags, ignoreWhitespace)

if __name__ == "__main__":
	lexer = Lexer([
		("word", "[a-z]+"),
		("shortdate", "\d{1,2}\/\d{1,2}\/\d{4}")
		], re.I)
	for token in lexer.scan("I was born on", True):
		print token