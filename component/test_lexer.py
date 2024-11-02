import unittest
from lexer import CustomLexerGenerator
from rply.token import Token
import json5


class TestLexerToken(unittest.TestCase):
 
    def setUp(self):
        SYNTAX_RULES_PATH = "../syntax_rules/syntax_rules.jsonc"
        with open(SYNTAX_RULES_PATH, "r") as file:
            syntax_rules = json5.load(file)
        my_lexer_generator = CustomLexerGenerator(syntax_rules=syntax_rules)
        self.lexer = my_lexer_generator.build()
    
    def test_template_token(self):
        _input = "template"
        expected = Token("TEMPLATE", "template")
        for token in self.lexer.lex(_input):
            self.assertEqual(token, expected)
    
    def test_function_token(self):
        _input = "fn"
        expected = Token("FUNCTION", "fn")
        for token in self.lexer.lex(_input):
            self.assertEqual(token, expected)
    
    def test_open_paranthesis_token(self):
        _input = "("
        expected = Token("OPEN_PARAN", "(")
        for token in self.lexer.lex(_input):
            self.assertEqual(token, expected)
    
    def test_close_paranthesis_token(self):
        _input = ")"
        expected = Token("CLOSE_PARAN", ")")
        for token in self.lexer.lex(_input):
            self.assertEqual(token, expected)
    
    def test_open_curly_bracket_token(self):
        _input = "{"
        expected = Token("OPEN_CURLY_BRACKET", "{")
        for token in self.lexer.lex(_input):
            self.assertEqual(token, expected)
    
    def test_close_curly_bracket_token(self):
        _input = "}"
        expected = Token("CLOSE_CURLY_BRACKET", "}")
        for token in self.lexer.lex(_input):
            self.assertEqual(token, expected)
    
    def test_comma_token(self):
        _input = ","
        expected = Token("COMMA", ",")
        for token in self.lexer.lex(_input):
            self.assertEqual(token, expected)
    
    def test_assignment_token(self):
        _input = "="
        expected = Token("ASSIGNMENT", "=")
        for token in self.lexer.lex(_input):
            self.assertEqual(token, expected)
    
    def test_semi_colon_token(self):
        _input = ";"
        expected = Token("SEMI_COLON", ";")
        for token in self.lexer.lex(_input):
            self.assertEqual(token, expected)
            
    def test_from_token(self):
        _input = "from"
        expected = Token("FROM", "from")
        for token in self.lexer.lex(_input):
            self.assertEqual(token, expected)
    
    def test_to_token(self):
        _input = "to"
        expected = Token("TO", "to")
        for token in self.lexer.lex(_input):
            self.assertEqual(token, expected)
    
    def test_as_token(self):
        _input = "as"
        expected = Token("AS", "as")
        for token in self.lexer.lex(_input):
            self.assertEqual(token, expected)
    
    def test_check_token(self):
        _input = "check"
        expected = Token("CHECK", "check")
        for token in self.lexer.lex(_input):
            self.assertEqual(token, expected)
    
    def test_finish_token(self):
        _input = "finish"
        expected = Token("FINISH", "finish")
        for token in self.lexer.lex(_input):
            self.assertEqual(token, expected)
    
    def test_int_type_token(self):
        _input = "int"
        expected = Token("TYPE", "int")
        for token in self.lexer.lex(_input):
            self.assertEqual(token, expected)
    
    def test_bol_type_token(self):
        _input = "bol"
        expected = Token("TYPE", "bol")
        for token in self.lexer.lex(_input):
            self.assertEqual(token, expected)
    
    def test_arr_int_type_token(self):
        _input = "arr<int>"
        expected = Token("TYPE", "arr<int>")
        for token in self.lexer.lex(_input):
            self.assertEqual(token, expected)
    
    def test_open_bracket_token(self):
        _input = "["
        expected = Token("OPEN_BRACKET", "[")
        for token in self.lexer.lex(_input):
            self.assertEqual(token, expected)
    
    def test_close_bracket_token(self):
        _input = "]"
        expected = Token("CLOSE_BRACKET", "]")
        for token in self.lexer.lex(_input):
            self.assertEqual(token, expected)
    
    def test_number_token(self):
        _input = "100"
        expected = Token("NUMBER", "100")
        for token in self.lexer.lex(_input):
            self.assertEqual(token, expected)
    
    def test_letter_token(self):
        _input = "a"
        expected = Token("LETTER", "a")
        for token in self.lexer.lex(_input):
            self.assertEqual(token, expected)
    
    def test_true_boolean_token(self):
        _input = "true"
        expected = Token("BOOLEAN", "true")
        for token in self.lexer.lex(_input):
            self.assertEqual(token, expected)
    
    def test_greater_than_operator_token(self):
        _input = ">"
        expected = Token("OPERATOR", ">")
        for token in self.lexer.lex(_input):
            self.assertEqual(token, expected)
    
    def test_less_than_operator_token(self):
        _input = "<"
        expected = Token("OPERATOR", "<")
        for token in self.lexer.lex(_input):
            self.assertEqual(token, expected)
    
    def test_equal_equal_operator_token(self):
        _input = "=="
        expected = Token("OPERATOR", "==")
        for token in self.lexer.lex(_input):
            self.assertEqual(token, expected)
    
    def test_not_equal_operator_token(self):
        _input = "!="
        expected = Token("OPERATOR", "!=")
        for token in self.lexer.lex(_input):
            self.assertEqual(token, expected)
    
    def test_plus_operator_token(self):
        _input = "+"
        expected = Token("OPERATOR", "+")
        for token in self.lexer.lex(_input):
            self.assertEqual(token, expected)
    
    def test_minus_operator_token(self):
        _input = "-"
        expected = Token("OPERATOR", "-")
        for token in self.lexer.lex(_input):
            self.assertEqual(token, expected)
    
    def test_multiply_operator_token(self):
        _input = "*"
        expected = Token("OPERATOR", "*")
        for token in self.lexer.lex(_input):
            self.assertEqual(token, expected)
    
    def test_divide_operator_token(self):
        _input = "/"
        expected = Token("OPERATOR", "/")
        for token in self.lexer.lex(_input):
            self.assertEqual(token, expected)
    
    def test_sharp_token(self):
        _input = "#"
        expected = Token("SHARP", "#")
        for token in self.lexer.lex(_input):
            self.assertEqual(token, expected)
    
    def test_exclamation_special_character_token(self):
        _input = "!"
        expected = Token("SPECIAL_CHARACTER", "!")
        for token in self.lexer.lex(_input):
            self.assertEqual(token, expected)
    
    def test_at_special_character_token(self):
        _input = "@"
        expected = Token("SPECIAL_CHARACTER", "@")
        for token in self.lexer.lex(_input):
            self.assertEqual(token, expected)
    
    def test_at_dollar_character_token(self):
        _input = "$"
        expected = Token("SPECIAL_CHARACTER", "$")
        for token in self.lexer.lex(_input):
            self.assertEqual(token, expected)
    
    def test_string_literal_token(self):
        _input = "\"hello world\""
        expected = Token("STRING_LITERAL", "\"hello world\"")
        for token in self.lexer.lex(_input):
            self.assertEqual(token, expected)
    
    def test_method_access_token(self):
        _input = "->"
        expected = Token("METHOD_ACCESS", "->")
        for token in self.lexer.lex(_input):
            self.assertEqual(token, expected)


class TestLexer(unittest.TestCase):
 
    def setUp(self):
        SYNTAX_RULES_PATH = "../syntax_rules/syntax_rules.jsonc"
        with open(SYNTAX_RULES_PATH, "r") as file:
            syntax_rules = json5.load(file)
        my_lexer_generator = CustomLexerGenerator(syntax_rules=syntax_rules)
        self.lexer = my_lexer_generator.build()
        
    # arr<int> numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1];    
    def test_arr_numbers(self):
        _input = "arr<int> numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1];"
        expected = [
            Token("TYPE", "arr<int>"),
            Token("LETTER", "n"),
            Token("LETTER", "u"),
            Token("LETTER", "m"),
            Token("LETTER", "b"),
            Token("LETTER", "e"),
            Token("LETTER", "r"),
            Token("LETTER", "s"),
            Token("ASSIGNMENT", "="),
            Token("OPEN_BRACKET", "["),
            Token("NUMBER", "9"),
            Token("COMMA", ","),
            Token("NUMBER", "8"),
            Token("COMMA", ","),
            Token("NUMBER", "7"),
            Token("COMMA", ","),
            Token("NUMBER", "6"),
            Token("COMMA", ","),
            Token("NUMBER", "5"),
            Token("COMMA", ","),
            Token("NUMBER", "4"),
            Token("COMMA", ","),
            Token("NUMBER", "3"),
            Token("COMMA", ","),
            Token("NUMBER", "2"),
            Token("COMMA", ","),
            Token("NUMBER", "1"),
            Token("CLOSE_BRACKET", "]"),
            Token("SEMI_COLON", ";"),
        ]
        for i, token in enumerate(self.lexer.lex(_input)):
            self.assertEqual(token, expected[i])
    
    # log("before:", numbers); 
    def test_log_before(self):
        _input = "log(\"before:\", numbers);"
        expected = [
            Token("LETTER", "l"),
            Token("LETTER", "o"),
            Token("LETTER", "g"),
            Token("OPEN_PARAN", "("),
            Token("STRING_LITERAL", "\"before:\""),
            Token("COMMA", ","),
            Token("LETTER", "n"),
            Token("LETTER", "u"),
            Token("LETTER", "m"),
            Token("LETTER", "b"),
            Token("LETTER", "e"),
            Token("LETTER", "r"),
            Token("LETTER", "s"),
            Token("CLOSE_PARAN", ")"),
            Token("SEMI_COLON", ";")
        ]
        for i, token in enumerate(self.lexer.lex(_input)):
            self.assertEqual(token, expected[i])


if __name__ == "__main__":
    unittest.main(verbosity=2)