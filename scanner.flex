%{
#include "token.h"

int count_line = 1;
%}

SPACE      [ \t\n]
NEWLINE    [ \n]
DIGIT      [0-9]
LETTER     [A-Za-z]
INT        (0|[1-9]{DIGIT}*)
%%
{SPACE}      {}
{NEWLINE}     { count_line++; }
{INT}         { return TOKEN_INT; }
%%

int yywrap() { return 1; }