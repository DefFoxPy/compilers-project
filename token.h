#pragma once

typedef enum
{
    TOKEN_EOF = 0,
    TOKEN_INT = 258,
    TOKEN_IDENTIFIER = 259,
    TOKEN_MOVE = 260,
    TOKEN_TURN_LEFT = 261,
    TOKEN_TURN_RIGHT = 262,
    TOKEN_LOOP = 263,
    TOKEN_LIGHT_UP = 264,
    TOKEN_PROCEDURE = 265,
    TOKEN_CALL = 266,
    TOKEN_LEFT_PAREN = 267,
    TOKEN_RIGHT_PAREN = 268,
    TOKEN_LEFT_BRACE = 269,
    TOKEN_RIGHT_BRACE = 270,
    TOKEN_COMMA = 271,
    TOKEN_EQUAL = 272,
    TOKEN_IF = 273,
    TOKEN_ELSE = 274
    
}
token_t;

inline const char* to_str(token_t t)
{
    switch (t)
    {
        case TOKEN_EOF: return "EOF";
        case TOKEN_INT: return "INTEGER";
        case TOKEN_IDENTIFIER: return "TOKEN_IDENTIFIER";
        case TOKEN_MOVE: return "MOVE";
        case TOKEN_TURN_LEFT: return "TURN LEFT";
        case TOKEN_TURN_RIGHT: return "TURN RIGHT";
        case TOKEN_LOOP: return "TOKEN_LOOP";
        case TOKEN_LIGHT_UP: return "TOKEN_LIGHT_UP";
        case TOKEN_PROCEDURE: return "TOKEN_PROCEDURE";
        case TOKEN_CALL: return "TOKEN_CALL";
        case TOKEN_LEFT_PAREN: return "TOKEN_LEFT_PAREN";
        case TOKEN_RIGHT_PAREN: return "TOKEN_RIGHT_PAREN";
        case TOKEN_LEFT_BRACE: return "TOKEN_LEFT_BRACE";
        case TOKEN_RIGHT_BRACE: return "TOKEN_RIGHT_BRACE";
        case TOKEN_COMMA: return "TOKEN_COMMA";
        case TOKEN_EQUAL: return "TOKEN_EQUAL";
        case TOKEN_IF: return "TOKEN_IF";
        case TOKEN_ELSE: return "TOKEN_ELSE";
    }
}