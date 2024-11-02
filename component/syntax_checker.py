import json5
from component.lexer import CustomLexerGenerator


# consists of Lexer and Parser
class SyntaxChecker():
    
	def __init__(self, syntax_rules_path="", includeLexerPrefix=True, verbose=False):
		"""
		Initialize the lexer and parser
		"""
		with open(syntax_rules_path, "r") as file:
			syntax_rules = json5.load(file)
			custom_lexer_generator = CustomLexerGenerator(syntax_rules=syntax_rules, includeLexerPrefix=includeLexerPrefix, verbose=verbose)
			self.lexer = custom_lexer_generator.build()

	def run(self):
	
		exitCommands = ["exit", "quit", "stop", "end"]

		while True:
			try:
				code_snippet = input("\n\nHantverk> ")

				if (code_snippet.lower() in exitCommands) or (code_snippet.lower()[0] == "q"):
					break
				
				# TODO change this after adding parser
				# eg self.parser.parse(self.lexer.lex(code_snippet))
				# -------------TEMP-----------------
				tokens = self.lexer.lex(code_snippet)

				for token in tokens:
					print(token)
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