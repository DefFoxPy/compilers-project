#pragma once

typedef enum
{
    TOKEN_EOF = 0,
    TOKEN_SELECT = 258,
}
token_t;

inline const char* to_str(token_t t)
{
    switch (t)
    {
        case TOKEN_SELECT: return "SELECT";
    }
}