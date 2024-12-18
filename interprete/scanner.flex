%{
#include <stdio.h>  
#include <string.h>
#include <string>

#include "token.h"

int count_line = 1;
int int_value = 0;
char* identi;

%}

SPACE      [ \t]
NEWLINE    [\n\r]
DIGIT      [0-9]
LETTER     [A-Za-z]
INT        (0|[1-9]{DIGIT}*)
IDENTIFIER (_|{LETTER})({DIGIT}|{LETTER}|_)*
MOVE       [Mm][Oo][Vv][Ee]
TURN_LEFT  [Tt][Uu][Rr][Nn][_][Ll][Ee][Ff][Tt]
TURN_RIGHT [Tt][Uu][Rr][Nn][_][Rr][Ii][Gg][Hh][Tt]
LOOP       [Ll][Oo][Oo][Pp]
LIGHT_UP   [Ll][Ii][Gg][Hh][Tt][_][Uu][Pp]
PROCEDURE  [Pp][Rr][Oo][Cc][Ee][Dd][Uu][Rr][Ee]
COMMENT    \/\/.* 


%%
{SPACE}       {}
{NEWLINE}     { count_line++; }
{INT}         { int_value = atoi(yytext); return TOKEN_INT; }
{MOVE}        { return TOKEN_MOVE; }
{TURN_LEFT}   { return TOKEN_TURN_LEFT; }
{TURN_RIGHT}  { return TOKEN_TURN_RIGHT; }
{LOOP}		  { return TOKEN_LOOP; }
{LIGHT_UP}    { return TOKEN_LIGHT_UP; }
{PROCEDURE}   { return TOKEN_PROCEDURE; }
"("           { return TOKEN_LEFT_PAREN; }
")"           { return TOKEN_RIGHT_PAREN; }
"{"           { return TOKEN_LEFT_BRACE; }
"}"           { return TOKEN_RIGHT_BRACE; }
{IDENTIFIER}  { yylval = strdup(yytext); identi = yylval; return TOKEN_IDENTIFIER; }
{COMMENT}     {}
.             { printf("Unexpected token in line %d - %s\n", count_line, yytext); }

%%

int yywrap() { return 1; }