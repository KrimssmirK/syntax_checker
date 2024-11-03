from component.lexer import MyLexer
from component.parser import MyParser
from component.syntax_checker import SyntaxChecker
import os


def main():
    syntax_checker = SyntaxChecker(lexer=MyLexer(), parser=MyParser())
    
    print(f"\n\n\033[0;37;40m{'-'*10}SYNTAX CHECK RESULT{'-'*10}")
    
    # read sample codes
    code_folder = "codes"
    code_files = os.listdir(code_folder)
    for filename in code_files:
        filepath = os.path.join(code_folder, filename)
        
        # read the code
        with open(filepath, "r") as file:
            code = file.read()
        
        print(f"{filename}: ", end="")
        
        # check the syntax
        syntax_checker.check(code)
        
        print("\033[0;37;40m")
 

if __name__ == "__main__":
	main()
