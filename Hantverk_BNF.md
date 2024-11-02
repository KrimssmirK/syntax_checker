```
<CodeChallenge> ::= "template" "CodeChallenge" "{" <Program> "}"

<Program> ::= <Function>* 

<Function> ::= "fn" <Identifier> "(" <ParameterList> ")" "{" <Comment>* <FunctionBody> "}"

<ParameterList> ::= <Parameter> | <Parameter> "," <ParameterList> | ""

<Parameter> ::= <Type> <Identifier>

<FunctionBody> ::= <Statement>* 

<Statement> ::= <VariableDeclaration>
              | <FunctionCall>
              | <ControlStatement>
              | <ReturnStatement>
              | <Comment>

<VariableDeclaration> ::= <Type> <Identifier> "=" <Expression> ";"

<FunctionCall> ::= <Identifier> "(" <ArgumentList> ")" ";"

<ControlStatement> ::= <LoopStatement>
                    | <ConditionStatement>

<LoopStatement> ::= "from" <Expression> "to" <Expression> "as" <Identifier> "{" <Comment>* <Statement>* "}"

<ConditionStatement> ::= "check" "(" <Expression> ")" "{" <Comment>* <Statement>* "}"

<ReturnStatement> ::= "finish;"  # Keyword to exit a function

<ArgumentList> ::= <Expression> | <Expression> "," <ArgumentList> | ""

<Type> ::= "int" | "bol" | "arr<int>"

<Expression> ::= <Identifier>
               | <Literal>
               | <Expression> <Operator> <Expression>
               | <ObjectAccess>

<Literal> ::= <ArrayLiteral> | <Number> | <Boolean> | <StringLiteral>

<ArrayLiteral> ::= "[" <ElementList> "]"

<ElementList> ::= <Expression> | <Expression> "," <ElementList> | ""

<Number> ::= <Digit>+

<Digit> ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"

<Identifier> ::= <Letter> <IdentifierTail>

<IdentifierTail> ::= <Letter> <IdentifierTail> | <Digit> <IdentifierTail> | ""

<Letter> ::= "a" | "b" | ... | "z" | "A" | "B" | ... | "Z"

<Boolean> ::= "true" | "false"

<StringLiteral> ::= "\"" <StringCharacter>* "\""
<StringCharacter> ::= <Letter> | <Digit> | <SpecialCharacter>  # Can include letters, digits, and special characters

<Operator> ::= ">" | "<" | "==" | "!=" | "+" | "-" | "*" | "/"

<ObjectAccess> ::= <Identifier> "->" <Identifier> "(" <ArgumentList> ")"
```