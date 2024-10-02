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
LIGHT_UP   [Ll][Ii][Gg][Hh][Tt][_][Uu][Pp]
PROCEDURE  [Pp][Rr][Oo][Cc][Ee][Dd][Uu][Ee]
CALL       [Cc][Aa][Ll][Ll]
LEFT_PAREN [(]
RIGHT_PAREN [)]
LEFT_BRACE [{]
RIGHT_BRACE [}]
COMMA      [,]
EQUAL      [=]
IF         [Ii][Ff]
ELSE       [Ee][Ll][Ss][Ee]

%%
{SPACE}       {}
{NEWLINE}     { count_line++; }
{INT}         { return TOKEN_INT; }
{MOVE}        { return TOKEN_MOVE; }
{TURN_LEFT}   { return TOKEN_TURN_LEFT; }
{TURN_RIGHT}  { return TOKEN_TURN_RIGHT; }
{LOOP}		  { return TOKEN_LOOP; }
{LIGHT_UP}    { return TOKEN_LIGHT_UP; }
{PROCEDURE}   { return TOKEN_PROCEDURE; }
{CALL}        { return TOKEN_CALL; }
{LEFT_PAREN}  { return TOKEN_LEFT_PAREN; }
{RIGHT_PAREN} { return TOKEN_RIGHT_PAREN; }
{LEFT_BRACE}  { return TOKEN_LEFT_BRACE; }
{RIGHT_BRACE} { return TOKEN_RIGHT_BRACE; }
{COMMA}       { return TOKEN_COMMA; }
{EQUAL}       { return TOKEN_EQUAL; }
{IF}          { return TOKEN_IF; }
{ELSE}        { return TOKEN_ELSE; }
{IDENTIFIER}  { return TOKEN_IDENTIFIER; }
.             { printf("Unexpected token in line %d\n", count_line); }
%%

int yywrap() { return 1; }