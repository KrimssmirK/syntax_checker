class SyntaxChecker():
    
	def __init__(self, lexer=None, parser=None):
		"""
		Initialize the lexer and parser
		"""
		self.lexer = lexer
		self.parser = parser

	def run_prompt(self):
	
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
    
	def check(self, code):
		"""_summary_

		Args:
			code (str): Hantverk Code Snippets e.g. template Player {}
		"""
			
		try:
			tokens = self.lexer.tokenize(code)
			self.parser.parse(tokens)
			print("\033[1;32;40mSYNTAX VALID!")
		except Exception as e:
			print("\n\033[1;31;40m======= ERROR =======")
			print(e)
			print("=====================\n")
        