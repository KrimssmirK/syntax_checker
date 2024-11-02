from rply import LexerGenerator
import json5


WHITESPACE=r"\s+"
TOKEN_DETAIL_IDX=1


class CustomLexerGenerator():
    
	def __init__(
     self, 
     syntax_rules=None, 
     includeLexerPrefix=True, 
     verbose=False
     ):
		if type(syntax_rules) is not dict:  raise Exception("Rules must be a dictionary")

		self.lexer = LexerGenerator()
		self.syntax_rules = syntax_rules
		self.includeLexerPrefix = includeLexerPrefix
		self.verbose = verbose

		if syntax_rules:
			self.are_rules_added = True
			self.add_syntax_rules(syntax_rules)
		else:
			self.are_rules_added = False

	def add_syntax_rules(self, syntax_rules):
		for token_name, re_pattern in syntax_rules.items():
			try:
				token_to_add = token_name if self.includeLexerPrefix else token_name.split("-")[TOKEN_DETAIL_IDX]

				if self.verbose: print(f"Adding token {self.syntax_rules[token_name]} as {token_to_add}")
    
				self.lexer.add(token_to_add, re_pattern)
			except Exception as e:
				print(f"Error adding token {self.syntax_rules[token_name]}: {e}")

		self.lexer.ignore(WHITESPACE)

	def build(self):
		if self.are_rules_added:
			return self.lexer.build()
		else:
			print("no rules are setup to the Lexer Generator")


def main():
    # Load the rules
	SYNTAX_RULES_PATH = "../syntax_rules/syntax_rules.jsonc"
	with open(SYNTAX_RULES_PATH, "r") as file:
		syntax_rules = json5.load(file)
  
	my_lexer_generator = CustomLexerGenerator(syntax_rules=syntax_rules)
	my_lexer = my_lexer_generator.build()
	_input = "# dasfds;"
	for token in my_lexer.lex(_input):
		print(token)
    

if __name__ == "__main__":
    main()
