from rply import ParserGenerator
from rply.token import Token


class MyParser:
    def __init__(self):
        self.pg = ParserGenerator(
            ['TEMPLATE', 'IDENTIFIER', 'LCBRACKET', 'RCBRACKET',
             "FUNCTION", "LPARAN", "RPARAN", "TYPE", "COMMA",
             "ASSIGN", "SEMICOLON", "NUMBER", "BOOLEAN",
             "STRING", "LBRACKET", "RBRACKET", "OPERATOR",
             "ARROW", "FROM", "TO", "AS", "CHECK", "FINISH",
             "COMMENT"
            ]
        )
        
        # Register productions
        self.register_productions()
        
        # build the parser
        self.parser = self.pg.build()

    def register_productions(self):
        """This is where the BNF is defined well"""
        
        @self.pg.production('program : class')
        def program(p):
            return {'type': 'program', 'template': p[0]}
        
        @self.pg.production('class : TEMPLATE IDENTIFIER LCBRACKET comment_list class_body RCBRACKET')
        def class_definition(p):
            return {'type': 'class', 'template': p}
        
        @self.pg.production('class_body : function class_body')
        def class_body_functions(p):
            return {'type': 'class_body', 'template': p}
        
        @self.pg.production('class_body :')
        def empty_class_body(p):
            return {'type': 'empty_class_body', 'template': p}
        
        @self.pg.production('function : FUNCTION IDENTIFIER LPARAN parameter_list RPARAN LCBRACKET function_body RCBRACKET')
        def function_definition(p):
            return {'type': 'function', 'template': p}
        
        @self.pg.production('parameter_list : parameter')
        def one_parameter_list(p):
            return {'type': 'one_parameter_list', 'template': p}
        
        @self.pg.production('parameter_list : parameter COMMA parameter_list')
        def multiple_parameter_list(p):
            return {'type': 'multiple_parameter_list', 'template': p}
        
        @self.pg.production('parameter_list :')
        def no_parameter_list(p):
            return {'type': 'no_parameter_list', 'template': p}
        
        @self.pg.production('parameter : TYPE IDENTIFIER')
        def parameter_definition(p):
            return {'type': 'parameter', 'template': p}
        
        @self.pg.production('function_body : statement_list')
        def function_body(p):
            return {'type': 'function_body', 'template': p}
        
        @self.pg.production('statement_list : statement')
        def one_statement_list(p):
            return {'type': 'one_statement_list', 'template': p}
        
        @self.pg.production('statement_list : statement statement_list')
        def multiple_statement_list(p):
            return {'type': 'one_statement_list', 'template': p}
       
        @self.pg.production('statement : variable_declaration')
        def statement_with_variable_declaration(p):
            return {'type': 'statement_with_variable_declaration', 'template': p}
        
        @self.pg.production('statement : variable_assignment')
        def statement_with_variable_assignment(p):
            return {'type': 'statement_with_variable_assignment', 'template': p}
        
        @self.pg.production('statement : function_call')
        def statement_with_function_call(p):
            return {'type': 'statement_with_function_call', 'template': p}
        
        @self.pg.production('statement : control_statement')
        def statement_with_control(p):
            return {'type': 'statement_with_control', 'template': p}
        
        @self.pg.production('statement : return_statement')
        def statement_with_return(p):
            return {'type': 'statement_with_return', 'template': p}
        
        @self.pg.production('statement : comment_list')
        def statement_with_comment(p):
            return {'type': 'statement_with_comment', 'template': p}
        
        @self.pg.production('statement :')
        def empty_statement(p):
            return {'type': 'empty_statement', 'template': p}
        
        @self.pg.production('function_call : IDENTIFIER LPARAN argument_list RPARAN SEMICOLON')
        def function_call(p):
            return {'type': 'function_call', 'template': p}
        
        @self.pg.production('control_statement : loop_statement')
        def control_statement_loop(p):
            return {'type': 'control_statement_loop', 'template': p}
        
        @self.pg.production('control_statement : condition_statement')
        def control_statement_condition(p):
            return {'type': 'control_statement_condition', 'template': p}
        
        @self.pg.production('return_statement : FINISH SEMICOLON')
        def return_statement(p):
            return {'type': 'return_statement', 'template': p}
        
        @self.pg.production('comment_list : COMMENT')
        def one_comment_list(p):
            return {'type': 'one_comment_list', 'template': p}
        
        @self.pg.production('comment_list : COMMENT comment_list')
        def multiple_comment_list(p):
            return {'type': 'multiple_comment_list', 'template': p}
        
        @self.pg.production('comment_list :')
        def no_comment_list(p):
            return {'type': 'no_comment_list', 'template': p}
        
        @self.pg.production('loop_statement : FROM expression TO expression AS IDENTIFIER LCBRACKET statement_list RCBRACKET')
        def loop_statement(p):
            return {'type': 'loop_statement', 'template': p}
        
        @self.pg.production('condition_statement : CHECK LPARAN expression RPARAN LCBRACKET statement_list RCBRACKET')
        def condition_statement(p):
            return {'type': 'condition_statement', 'template': p}
        
        @self.pg.production('variable_declaration : TYPE IDENTIFIER ASSIGN expression SEMICOLON')
        def variable_declaration(p):
            return {'type': 'variable_declaration', 'template': p}
        
        @self.pg.production('variable_assignment : IDENTIFIER ASSIGN expression SEMICOLON')
        def variable_assignment(p):
            return {'type': 'variable_assignment', 'template': p}
        
        @self.pg.production('variable_assignment : array_access ASSIGN expression SEMICOLON')
        def variable_assignment_array(p):
            return {'type': 'variable_assignment', 'template': p}
        
        @self.pg.production('expression : IDENTIFIER')
        def expression_identifier(p):
            return {'type': 'expression_identifier', 'template': p}
        
        @self.pg.production('expression : literal')
        def expression_literal(p):
            return {'type': 'expression_literal', 'template': p}
        
        @self.pg.production('expression : array_access')
        def expression_array_access(p):
            return {'type': 'expression_array_access', 'template': p}
        
        @self.pg.production('expression : expression OPERATOR expression')
        def expression_with_operator(p):
            return {'type': 'expression_with_operator', 'template': p}
        
        @self.pg.production('expression : object_access')
        def expression_object_access(p):
            return {'type': 'expression_object_access', 'template': p}
        
        @self.pg.production('literal : NUMBER')
        def literal_number(p):
            return {'type': 'literal_number', 'template': p}
        
        @self.pg.production('literal : BOOLEAN')
        def literal_boolean(p):
            return {'type': 'literal_boolean', 'template': p}
        
        @self.pg.production('literal : STRING')
        def literal_string(p):
            return {'type': 'literal_string', 'template': p}
        
        @self.pg.production('literal : array_literal')
        def literal_array(p):
            return {'type': 'literal_array', 'template': p}
        
        @self.pg.production('array_literal : LBRACKET element_list RBRACKET')
        def array_literal(p):
            return {'type': 'array_literal', 'template': p}
        
        @self.pg.production('array_access :  IDENTIFIER LBRACKET expression RBRACKET ')
        def array_access(p):
            return {'type': 'array_access', 'template': p}
        
        @self.pg.production('element_list : expression')
        def one_element_list(p):
            return {'type': 'one_element_list', 'template': p}
        
        @self.pg.production('element_list : expression COMMA element_list')
        def multiple_element_list(p):
            return {'type': 'multiple_element_list', 'template': p}
        
        @self.pg.production('element_list :')
        def none_element_list(p):
            return {'type': 'none_element_list', 'template': p}
        
        @self.pg.production('object_access : IDENTIFIER ARROW IDENTIFIER LPARAN argument_list RPARAN')
        def object_access(p):
            return {'type': 'object_access', 'template': p}
        
        @self.pg.production('argument_list : expression')
        def one_argument_list(p):
            return {'type': 'one_argument_list', 'template': p}
        
        @self.pg.production('argument_list : expression COMMA argument_list')
        def multiple_argument_list(p):
            return {'type': 'multiple_argument_list', 'template': p}
        
        @self.pg.production('argument_list :')
        def no_argument_list(p):
            return {'type': 'no_argument_list', 'template': p}
        
        # Handling Errors
        @self.pg.error
        def error_handler(token):
            if Token('IDENTIFIER', 'arr') == token:
                raise ValueError(f"Error in line {token.getsourcepos().lineno} at column {token.getsourcepos().colno}\nyou have a problem with arr!!\nTry to check either indexing or declaring an array")
            if Token('IDENTIFIER', 'fun') == token:
                raise ValueError(f"Error in line {token.getsourcepos().lineno} at column {token.getsourcepos().colno}\nyou have a problem with declaring a function!!\nUse the keyword \"fn\" when declaring a function")
            raise ValueError("Ran into a %s where it wasn't expected" % token)

    def parse(self, tokens):
        return self.parser.parse(tokens)