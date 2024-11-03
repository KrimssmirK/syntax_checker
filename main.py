from component.lexer import MyLexer
from component.parser import MyParser
from component.syntax_checker import SyntaxChecker

"""
SAMPLE INPUT:

check (myVar == 5) { ary->push(myVar); }

arr<str> ary = ["Hello", "World"];

int x = 1;
"""
def main():
	SyntaxChecker(
     lexer=MyLexer(), 
     parser=MyParser()
    ).run()
 

if __name__ == "__main__":
	main()
