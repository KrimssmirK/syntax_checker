```
<Program> ::= <Class>

<Class> ::= "template" <Identifier> "{" <ClassBody> "}"

<ClassBody> ::= <Function> <ClassBody> | ε

<Function> ::= "fn" <Identifier> "(" <ParameterList> ")" "{" <FunctionBody> "}"

<ParameterList> ::= <Parameter> | <Parameter> "," <ParameterList> | ε

<Parameter> ::= <Type> <Identifier>

<FunctionBody> ::= <StatementList>

<StatementList> ::= <Statement> | <Statement> <StatementList>

<Statement> ::= <VariableDeclaration>
              | <FunctionCall>
              | <ControlStatement>
              | <ReturnStatement>
              | <CommentList>
              | ε

<VariableDeclaration> ::= <Type> <Identifier> "=" <Expression> ";"

<FunctionCall> ::= <Identifier> "(" <ArgumentList> ")" ";"

<ControlStatement> ::= <LoopStatement>
                    | <ConditionStatement>

<ReturnStatement> ::= "finish" ";"

<LoopStatement> ::= "from" <Expression> "to" <Expression> "as" <Identifier> "{" <Statement>"}"

<ConditionStatement> ::= "check" "(" <Expression> ")" "{" <Statement> "}"

<CommentList> ::= <Comment> | <Comment> <CommentList>

<Expression> ::= <Identifier>
               | <Literal>
               | <Expression> <Operator> <Expression>
               | <ObjectAccess>

<Literal> ::= <ArrayLiteral> | <Number> | <Boolean> | <StringLiteral>

<ArrayLiteral> ::= "[" <ElementList> "]"

<ElementList> ::= <Expression> | <Expression> "," <ElementList> | ε

<ObjectAccess> ::= <Identifier> "->" <Identifier> "(" <ArgumentList> ")"

<ArgumentList> ::= <Expression> | <Expression> "," <ArgumentList> | ε
```