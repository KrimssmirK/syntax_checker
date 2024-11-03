from rply import LexerGenerator


class MyLexer():
    
	def __init__(self):
		self.lexer = LexerGenerator()

		# add rules
		self.lexer.add("TEMPLATE", r"template")
		self.lexer.add("FUNCTION", r"fn")
		self.lexer.add("FROM", r"from")
		self.lexer.add("TO", r"to")
		self.lexer.add("AS", r"as")
		self.lexer.add("CHECK", r"check")
		self.lexer.add("FINISH", r"finish")
		self.lexer.add("NUMBER", r"\d+")
		self.lexer.add("BOOLEAN", r"true|false")
		self.lexer.add("ARROW", r"->")
		self.lexer.add("STRING", r"\".*\"")
		self.lexer.add("TYPE", r"int|bol|arr<int>")
		self.lexer.add("COMMENT", r"#.*;")
		self.lexer.add("IDENTIFIER", r"[a-zA-Z0-9_][a-zA-Z0-9_]*")
		self.lexer.add("OPERATOR", r">|<|={2}|!=|\+|-{1}|\*|/")
		self.lexer.add("ASSIGN", r"=")
		self.lexer.add("SEMICOLON", r";")
		self.lexer.add("COMMA", r",")
		self.lexer.add("LBRACKET", r"\[")
		self.lexer.add("RBRACKET", r"\]")
		self.lexer.add("LCBRACKET", r"\{")
		self.lexer.add("RCBRACKET", r"\}")
		self.lexer.add("LPARAN", r"\(")
		self.lexer.add("RPARAN", r"\)")
		self.lexer.ignore(r"\s+")
		
		self.lexer = self.lexer.build()

	def tokenize(self, code):
		return self.lexer.lex(code)
