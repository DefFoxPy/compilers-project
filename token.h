#pragma once

typedef enum
{
    TOKEN_EOF = 0,
    TOKEN_INT = 258,
    
}
token_t;

inline const char* to_str(token_t t)
{
    switch (t)
    {
        case TOKEN_EOF: return "EOF";
        case TOKEN_INT: return "INTEGER";
    }
}