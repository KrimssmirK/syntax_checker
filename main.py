from component.syntax_checker import SyntaxChecker

"""
SAMPLE INPUT:

check (myVar == 5) { ary->push(myVar); }

arr<str> ary = ["Hello", "World"];

int x = 1;
"""
def main():
	SYNTAX_RULES_PATH = "syntax_rules/syntax_rules.jsonc"
	checker = SyntaxChecker(syntax_rules_path=SYNTAX_RULES_PATH)
	checker.run()
 
 
if __name__ == "__main__":
	main()
