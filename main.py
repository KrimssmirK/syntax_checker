from component.syntax_checker import SyntaxChecker

"""
SAMPLE INPUT:

check (myVar == 5) { ary->push(myVar); }

arr<str> ary = ["Hello", "World"];

int x = 1;
"""
def main():
	SyntaxChecker().run()
 

if __name__ == "__main__":
	main()
