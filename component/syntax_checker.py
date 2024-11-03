class SyntaxChecker():
    
	def __init__(self, lexer=None, parser=None):
		"""
		Initialize the lexer and parser
		"""
		self.lexer = lexer
		self.parser = parser

	def run(self):
	
		exitCommands = ["exit", "quit", "stop", "end"]

		while True:
			code_snippet = input("\n\nHantverk> ")
			if (code_snippet.lower() in exitCommands) or (code_snippet.lower()[0] == "q"):
				break
			
			try:
				tokens = self.lexer.tokenize(code_snippet)
				self.parser.parse(tokens)
				print("SYNTAX VALID!")
     			# ----------------------------------
			except Exception as e:
				print("\n======= ERROR =======")
				print(e)
				print("=====================\n")