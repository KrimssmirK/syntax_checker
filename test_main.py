from rply import LexerGenerator, ParserGenerator

# Define the lexer
class MyLexer:
    def __init__(self):
        self.lexer = LexerGenerator()

        # Add tokens
        self.lexer.add('TEMPLATE', r'template')
        self.lexer.add('LBRACE', r'\{')
        self.lexer.add('RBRACE', r'\}')
        self.lexer.add('ID', r'[a-zA-Z_][a-zA-Z0-9_]*')
        self.lexer.add('ASSIGN', r'=')
        self.lexer.add('SEMICOLON', r';')
        self.lexer.add('NUMBER', r'\d+')
        self.lexer.add('TRUE', r'true')
        self.lexer.add('FALSE', r'false')
        self.lexer.add('STRING', r'"[^"]*"')
        self.lexer.add('COMMENT', r'#.*')
        self.lexer.add('ARR', r'arr<int>')
        self.lexer.add('COMMA', r',')  # Add the COMMA token
        self.lexer.ignore(r'\s+')

        # Build the lexer
        self.lexer = self.lexer.build()

    def tokenize(self, code):
        return self.lexer.lex(code)


# Define the parser
class MyParser:
    def __init__(self):
        self.pg = ParserGenerator(
            ['TEMPLATE', 'LBRACE', 'RBRACE', 'ID', 'ASSIGN', 
             'SEMICOLON', 'NUMBER', 'TRUE', 'FALSE', 'STRING', 
             'COMMENT', 'ARR', 'COMMA']
        )
        
        # Register productions
        self.register_productions()

    def register_productions(self):
        @self.pg.production('program : template')
        def program(p):
            return {'type': 'program', 'template': p[0]}

        @self.pg.production('template : TEMPLATE ID LBRACE template_body RBRACE')
        def template(p):
            return {'type': 'template', 'name': p[1].getstr(), 'body': p[3]}

        @self.pg.production('template_body : statement template_body')
        def template_body(p):
            return {'type': 'template_body', 'statements': [p[0]] + p[1]['statements']}

        @self.pg.production('template_body :')
        def empty_template_body(p):
            return {'type': 'template_body', 'statements': []}

        @self.pg.production('statement : variable_declaration SEMICOLON')
        def statement_variable_declaration(p):
            return {'type': 'variable_declaration', 'declaration': p[0]}

        @self.pg.production('statement : function_declaration SEMICOLON')
        def statement_function_declaration(p):
            return {'type': 'function_declaration', 'declaration': p[0]}

        @self.pg.production('statement : COMMENT')
        def statement_comment(p):
            return {'type': 'comment', 'content': p[0].getstr()}

        @self.pg.production('variable_declaration : ARR ID ASSIGN array_literal')
        def variable_declaration_array(p):
            return {'type': 'variable_declaration', 'name': p[1].getstr(), 'value': p[3]}

        @self.pg.production('variable_declaration : ID ASSIGN expression')
        def variable_declaration(p):
            return {'type': 'variable_declaration', 'name': p[0].getstr(), 'value': p[2]}

        @self.pg.production('function_declaration : ID LBRACE RBRACE')
        def function_declaration(p):
            return {'type': 'function_declaration', 'name': p[0].getstr(), 'parameters': []}

        @self.pg.production('function_declaration : ID LBRACE template_body RBRACE')
        def function_declaration_with_body(p):
            return {'type': 'function_declaration', 'name': p[0].getstr(), 'body': p[2]}

        @self.pg.production('expression : NUMBER')
        def expression_number(p):
            return {'type': 'number', 'value': int(p[0].getstr())}

        @self.pg.production('expression : TRUE')
        def expression_true(p):
            return {'type': 'boolean', 'value': True}

        @self.pg.production('expression : FALSE')
        def expression_false(p):
            return {'type': 'boolean', 'value': False}

        @self.pg.production('expression : STRING')
        def expression_string(p):
            return {'type': 'string', 'value': p[0].getstr()}

        @self.pg.production('expression : ID LBRACE RBRACE')
        def function_call(p):
            return {'type': 'function_call', 'name': p[0].getstr(), 'args': []}

        @self.pg.production('array_literal : LBRACE expression_list RBRACE')
        def array_literal(p):
            return {'type': 'array_literal', 'elements': p[1]}

        @self.pg.production('expression_list : expression')
        def expression_list_single(p):
            return [p[0]]

        @self.pg.production('expression_list : expression COMMA expression_list')
        def expression_list_multiple(p):
            return [p[0]] + p[2]

    def parse(self, code):
        lexer = MyLexer().tokenize(code)
        parser = self.pg.build()
        return parser.parse(lexer)


# Example usage
if __name__ == '__main__':
    code = '''
    template CodeChallenge {
        # this is the start point of the program when this template invoked;
        fn main() {
            arr<int> numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1];
            log("before:", numbers);
            bubbleSort(numbers);
            log("after:", numbers);
        }

        fn bubbleSort(arr<int> numbers) {
            # get the length of the array;
            int n = numbers->size;

            # traverse through all array elements;
            from 0 to n as i {
                bol swapped = false;

                # last i elements are already in place;
                from 0 to n-i-1 as j {

                    # traverse the array from 0 to n-i-1;
                    # swap if the element found is greater;
                    # than the next element;
                    check (numbers[j] > arr[j+1]) {
                        swap(numbers, j, j+1);
                        swapped = true;
                    }
                }
                check (swapped == false) {
                    finish;
                }
            }
        }

        fn swap(arr<int> numbers, int i, int j) {
            int temp = numbers[i];
            numbers[i] = numbers[j];
            numbers[j] = temp;
        }
    }
    '''

    parser = MyParser()
    result = parser.parse(code)
    print(result)
