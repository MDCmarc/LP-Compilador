grammar Funx;

root
    : function* expression? EOF;

function
    : ID parameters LLI instruction+ LLD
    ;

parameters 
    : VAR*;

instruction 
    : conditional 
    | loop 
    | assignation
    | expression
    ;

conditional
    : IF condition LLI instruction+ LLD ELSE LLI instruction+ LLD #IfElse
    | IF condition LLI instruction+ LLD                           #If
    ;

loop: WHILE condition LLI instruction+ LLD;

condition
    : expression EQUAL expression         #Equal
    | expression NOTEQUAL expression      #NotEqual 
    | expression GREATER expression       #Greater
    | expression LESS expression          #Less
    | expression GREATEREQUAL expression  #GreaterEqual
    | expression LESSEQUAL expression     #LessEqual
    ;

assignation: VAR ASSIGN expression;

expression 
    : PI expression PD                           # Parentesis
    | <assoc=right> expression POWER expression  # Power
    | expression TIMES expression                # Multiplication
    | expression DIVIDE expression               # Division
    | <assoc=right> expression MOD expression    # Modulus
    | expression PLUS expression                 # Plus
    | expression MINUS expression                # Minus 
    | ID expression*                             # CallFunction
    | NUM                                        # Valor
    | VAR                                        # Variable
    ;


IF : 'if' ;
ELSE: 'else' ;
WHILE: 'while' ;

ASSIGN : '<-';
POWER : '^';
PLUS: '+';
MINUS:'-';
TIMES: '*' ;
DIVIDE: '/' ;
MOD: '%' ;

EQUAL : '=' ;
NOTEQUAL : '!=' ;
GREATER : '>' ;
LESS : '<';
GREATEREQUAL : '>=';
LESSEQUAL : '<=';

LLI: '{';
LLD: '}' ;

PI:'(';
PD:')';


NUM : [0-9]+ ;
VAR : [a-z][a-zA-Z0-9]* ;
ID  : [A-Z][a-zA-Z0-9]* ;

WS : [ \n\t\r]+ -> skip ;
COMENTARIO : '#'~[\r\n]* -> skip;

