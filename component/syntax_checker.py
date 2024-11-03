import json5
from component.lexer import MyLexer
from component.parser import MyParser


# consists of Lexer and Parser
class SyntaxChecker():
    
	def __init__(self, syntax_rules_path="", includeLexerPrefix=True, verbose=False):
		"""
		Initialize the lexer and parser
		"""
		self.lexer = MyLexer()
		self.parser = MyParser()

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



def main():
    SYNTAX_RULES_PATH = "../syntax_rules/syntax_rules.jsonc"
    syntax_checker = SyntaxChecker(syntax_rules_path=SYNTAX_RULES_PATH, verbose=True)
    syntax_checker.run()


if __name__ == "__main__":
    main()