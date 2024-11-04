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
				print(f"\n{'='*50} ERROR {'='*50}")
				print(e)
				print(f"{'='*107}\n")
    
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
			print(f"\n\033[1;31;40m{'='*50} ERROR {'='*50}")
			print(e)
			print(f"{'='*107}\n")
        