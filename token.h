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
    TOKEN_FINISH = 264,
    TOKEN_IF = 265,
    TOKEN_ELSE = 266
    
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
        case TOKEN_FINISH: return "TOKEN_FINISH";
        case TOKEN_IF: return "TOKEN_IF";
        case TOKEN_ELSE: return "TOKEN_ELSE";
    }
}