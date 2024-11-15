%{
#include <stdio.h>
#include <stdlib.h>

extern int yylex();
extern int count_line;
int yyerror(const char*);
%}

%token TOKEN_EOF
%token TOKEN_INT
%token TOKEN_IDENTIFIER
%token TOKEN_MOVE
%token TOKEN_TURN_LEFT
%token TOKEN_TURN_RIGHT
%token TOKEN_LOOP
%token TOKEN_LIGHT_UP
%token TOKEN_PROCEDURE
%token TOKEN_CALL
%token TOKEN_LEFT_PAREN
%token TOKEN_RIGHT_PAREN
%token TOKEN_LEFT_BRACE
%token TOKEN_RIGHT_BRACE

%%

program : procedure;

procedure : TOKEN_PROCEDURE TOKEN_IDENTIFIER TOKEN_LEFT_PAREN 
            TOKEN_RIGHT_PAREN TOKEN_LEFT_BRACE commands TOKEN_RIGHT_BRACE  
     ;

commands : commands command 
     | command
     ;

command : TOKEN_MOVE TOKEN_LEFT_PAREN TOKEN_RIGHT_PAREN
       | TOKEN_TURN_LEFT TOKEN_LEFT_PAREN TOKEN_RIGHT_PAREN
       | TOKEN_TURN_RIGHT TOKEN_LEFT_PAREN TOKEN_RIGHT_PAREN
       | TOKEN_LIGHT_UP TOKEN_LEFT_PAREN TOKEN_RIGHT_PAREN
       | TOKEN_LOOP TOKEN_LEFT_PAREN TOKEN_INT TOKEN_RIGHT_PAREN 
         TOKEN_LEFT_BRACE commands TOKEN_RIGHT_BRACE 
         
       | TOKEN_CALL TOKEN_IDENTIFIER TOKEN_LEFT_PAREN TOKEN_RIGHT_PAREN
       ;   
%%

int yyerror(const char* s)
{
    printf("Parse error at line %d: %s\n", count_line, s);
    return 1;
}