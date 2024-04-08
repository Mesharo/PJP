grammar projektLanguage;

program: statement+ EOF ;

statement : ';'
          | '{' statement* '}'
          | WHILE '(' expression ')' statement
          | (INT | FLOAT | STRING | BOOL) IDENTIFIER (',' IDENTIFIER)* ';'
          | READ IDENTIFIER (',' IDENTIFIER)* ';'
          | WRITE expression (',' expression)* ';'
          | IF '(' expression ')' statement (ELSE statement)?
          ;

expression : '(' expression ')'
           | IDENTIFIER
           | literal
           | prefix=('!'|'-') expression
           | expression bop=('*'|'/'|'%') expression
           | expression bop=('+'|'-'|'.') expression
           | expression bop=('>'|'<') expression
           | expression bop=('=='|'!=') expression
           | expression bop='&&' expression
           | expression bop='||' expression
           | <assoc=right> IDENTIFIER'=' expression
           ;

literal : INT_LITERAL 
        | FLOAT_LITERAL 
        | BOOL_LITERAL 
        | STRING_LITERAL 
        ;

WHILE : 'while' ;
INT : 'int' ;
FLOAT : 'float' ;
STRING : 'string' ;
BOOL : 'bool' ;
READ : 'read' ;
WRITE : 'write' ;
IF : 'if' ;
ELSE : 'else' ;

INT_LITERAL : [0-9]+ ;
FLOAT_LITERAL : [0-9]+ '.' [0-9+] ;
BOOL_LITERAL : ('true'|'false') ;
STRING_LITERAL : '"' (~["\r\n])* '"';

IDENTIFIER : [a-zA-Z$_] [a-zA-Z0-9]* ;

WS : [ \t\r\n]+ -> skip ;
LINE_COMMENT: '//' ~[\r\n]* -> skip ;