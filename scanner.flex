%{
#include "token.h"

int count_line = 1;
%}

SPACE      [ \t]
NEWLINE    [\n]
DIGIT      [0-9]
LETTER     [A-Za-z]
INT        (0|[1-9]{DIGIT}*)
IDENTIFIER (_|{LETTER})({DIGIT}|{LETTER}|_)*
MOVE       [Mm][Oo][Vv][Ee]
TURN_LEFT  [Tt][Uu][Rr][Nn][_][Ll][Ee][Ff][Tt]
TURN_RIGHT [Tt][Uu][Rr][Nn][_][Rr][Ii][Gg][Hh][Tt]
LOOP       [Ll][Oo][Oo][Pp]
FINISH     [Ff][Ii][Nn][Ii][Ss][Hh]
IF         [Ii][Ff]
ELSE       [Ee][Ll][Ss][Ee]
DEF        [Dd][Ee][Ff]

%%
{SPACE}       {}
{NEWLINE}     { count_line++; }
{INT}         { return TOKEN_INT; }
{MOVE}        { return TOKEN_MOVE; }
{TURN_LEFT}   { return TOKEN_TURN_LEFT; }
{TURN_RIGHT}  { return TOKEN_TURN_RIGHT; }
{LOOP}		  { return TOKEN_LOOP; }
{FINISH}      { return TOKEN_FINISH; }
{IF}          { return TOKEN_IF; }
{ELSE}        { return TOKEN_ELSE; }
{IDENTIFIER}  { return TOKEN_IDENTIFIER; }
.             { printf("Unexpected token in line %d\n", count_line); }
%%

int yywrap() { return 1; }