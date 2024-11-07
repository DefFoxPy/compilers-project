%{
#include <stdio.h>
#include <stdlib.h>
#include "commands.hpp"  

#define YYSTYPE Command* 

extern int yylex();
extern char* yytext;
int yyerror(const char*);
Command* parser_result{nullptr}; 

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
%token TOKEN_IF
%token TOKEN_ELSE

%%

program : procedure                                                             { parser_result = $1; }
        ;

procedure : TOKEN_PROCEDURE TOKEN_IDENTIFIER TOKEN_LEFT_PAREN 
            TOKEN_RIGHT_PAREN TOKEN_LEFT_BRACE commands TOKEN_RIGHT_BRACE       { $$ = new Procedure(yytext, dynamic_cast<CommandList*>($6)); }
          ;

commands : commands command                                                     { $$ = dynamic_cast<CommandList*>($1); $1->addCommand($2); }
         | command                                                              { $$ = new CommandList(); $$->addCommand($1); }
         ;

command : TOKEN_MOVE TOKEN_LEFT_PAREN TOKEN_RIGHT_PAREN                         { $$ = new Move(); }
        | TOKEN_TURN_LEFT TOKEN_LEFT_PAREN TOKEN_RIGHT_PAREN                    { $$ = new TurnLeft(); }
        | TOKEN_TURN_RIGHT TOKEN_LEFT_PAREN TOKEN_RIGHT_PAREN                   { $$ = new TurnRight(); }
        | TOKEN_LIGHT_UP TOKEN_LEFT_PAREN TOKEN_RIGHT_PAREN                     { $$ = new LightUp(); }
        | TOKEN_LOOP TOKEN_LEFT_PAREN TOKEN_INT TOKEN_RIGHT_PAREN 
          TOKEN_LEFT_BRACE commands TOKEN_RIGHT_BRACE                           { $$ = new Loop(atoi(yytext), dynamic_cast<CommandList*>($6)); }

        | TOKEN_CALL TOKEN_IDENTIFIER TOKEN_LEFT_PAREN TOKEN_RIGHT_PAREN        { $$ = new ProcedureCall(yytext); }
        ;

%%

int yyerror(const char* s)
{
    printf("Parse error: %s\n", s);
    return 1;
}
