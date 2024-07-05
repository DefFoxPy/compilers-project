#pragma once

typedef enum
{
    TOKEN_EOF = 0,
    TOKEN_INT = 258,
    TOKEN_MOVE = 259,
    TOKEN_TURN_LEFT = 260,
    TOKEN_TURN_RIGHT = 261
    
}
token_t;

inline const char* to_str(token_t t)
{
    switch (t)
    {
        case TOKEN_EOF: return "EOF";
        case TOKEN_INT: return "INTEGER";
        case TOKEN_MOVE: return "MOVE";
        case TOKEN_TURN_LEFT: return "TURN LEFT";
        case TOKEN_TURN_RIGHT: return "TURN RIGHT";
    }
}