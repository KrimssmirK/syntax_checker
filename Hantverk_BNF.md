```
<Program> ::= <Class>

<Class> ::= "template" <Identifier> "{" <CommentList> <ClassBody> "}"

<ClassBody> ::= <Function> <ClassBody> | ε

<Function> ::= "fn" <Identifier> "(" <ParameterList> ")" "{" <FunctionBody> "}"

<ParameterList> ::= <Parameter> | <Parameter> "," <ParameterList> | ε

<Parameter> ::= <Type> <Identifier>

<FunctionBody> ::= <StatementList>

<StatementList> ::= <Statement> | <Statement> <StatementList>

<Statement> ::= <VariableDeclaration>
              | <VariableAssignment>
              | <FunctionCall>
              | <ControlStatement>
              | <ReturnStatement>
              | <CommentList>
              | ε

<VariableDeclaration> ::= <Type> <Identifier> "=" <Expression> ";"

<VariableAssignment> ::= <Identifier> "=" <Expression> ";"
                       | <ArrayAccess> "=" <Expression> ";"

<FunctionCall> ::= <Identifier> "(" <ArgumentList> ")" ";"

<ControlStatement> ::= <LoopStatement>
                    | <ConditionStatement>

<ReturnStatement> ::= "finish" ";"

<LoopStatement> ::= "from" <Expression> "to" <Expression> "as" <Identifier> "{" <StatementList>"}"

<ConditionStatement> ::= "check" "(" <Expression> ")" "{" <StatementList> "}"

             
<CommentList> ::= <Comment> | <Comment> <CommentList> | ε

<Expression> ::= <Identifier>
               | <Literal>
               | <ArrayAccess>
               | <Expression> <Operator> <Expression>
               | <ObjectAccess>

<Literal> ::= <ArrayLiteral> | <Number> | <Boolean> | <StringLiteral>

<ArrayAccess> ::= <Identifier> "[" <Expression> "]"

<ArrayLiteral> ::= "[" <ElementList> "]"

<ElementList> ::= <Expression> | <Expression> "," <ElementList> | ε

<ObjectAccess> ::= <Identifier> "->" <Identifier> "(" <ArgumentList> ")"

<ArgumentList> ::= <Expression> | <Expression> "," <ArgumentList> | ε
```