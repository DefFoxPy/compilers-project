%{
#include <stdio.h>
#include <stdlib.h>
#include <map>
#include "commands.hpp"  

#define YYSTYPE Command* 

extern int yylex();
extern char* yytext;
extern int count_line;
extern int int_value;
extern char* identi;     
int yyerror(const char*);
Command* parser_result{nullptr}; 

std::map<std::string, CustomFunction*> functionMap;

void addFunction(CustomFunction* func) {
    functionMap[func->getName()] = func; 
}

CustomFunction* findFunction(const std::string& name) {
    auto it = functionMap.find(name);
    if (it != functionMap.end()) {
        return it->second;
    }
    return nullptr;
}      
%}

%define api.value.type { char* }

%token TOKEN_EOF
%token TOKEN_INT
%token TOKEN_MOVE
%token TOKEN_TURN_LEFT
%token TOKEN_TURN_RIGHT
%token TOKEN_LOOP
%token TOKEN_LIGHT_UP
%token TOKEN_PROCEDURE
%token TOKEN_LEFT_PAREN
%token TOKEN_RIGHT_PAREN
%token TOKEN_LEFT_BRACE
%token TOKEN_RIGHT_BRACE
%token TOKEN_IDENTIFIER
%token TOKEN_FUNCTION
%token TOKEN_CALL


%%

program : custom_function procedure {parser_result = $1; }
        | procedure { parser_result = $1; }       
        ;


procedure : TOKEN_PROCEDURE TOKEN_IDENTIFIER TOKEN_LEFT_PAREN 
            TOKEN_RIGHT_PAREN TOKEN_LEFT_BRACE commands TOKEN_RIGHT_BRACE       { $$ = new Procedure(identi, dynamic_cast<CommandList*>($6)); } 
          ;

custom_function : TOKEN_FUNCTION TOKEN_IDENTIFIER TOKEN_LEFT_PAREN TOKEN_RIGHT_PAREN TOKEN_LEFT_BRACE commands TOKEN_RIGHT_BRACE {
            CustomFunction* func = new CustomFunction(identi, dynamic_cast<CommandList*>($6));
            addFunction(func);
            $$ = func; }
        | %empty
        ;

commands :
    commands command { 
        CommandList* cmdList = dynamic_cast<CommandList*>($1);
        CommandList* cmdList2 = new CommandList();

        if (cmdList) {
            cmdList->addCommand($2);
            $$ = cmdList;
        } else {
            cmdList2->addCommand($2); 
            $$ = cmdList2;
        }
    }
    | command {
        CommandList* newList = new CommandList();
        newList->addCommand($1);
        $$ = newList;
    }

;


command : TOKEN_MOVE TOKEN_LEFT_PAREN TOKEN_RIGHT_PAREN                         { $$ = new Move(); }
        | TOKEN_TURN_LEFT TOKEN_LEFT_PAREN TOKEN_RIGHT_PAREN                    { $$ = new TurnLeft(); }
        | TOKEN_TURN_RIGHT TOKEN_LEFT_PAREN TOKEN_RIGHT_PAREN                   { $$ = new TurnRight(); }
        | TOKEN_LIGHT_UP TOKEN_LEFT_PAREN TOKEN_RIGHT_PAREN                     { $$ = new LightUp(); }
        | TOKEN_LOOP TOKEN_LEFT_PAREN TOKEN_INT TOKEN_RIGHT_PAREN TOKEN_LEFT_BRACE commands TOKEN_RIGHT_BRACE     { $$ = new Loop(int_value, dynamic_cast<CommandList*>($6)); }
        | TOKEN_CALL TOKEN_IDENTIFIER TOKEN_LEFT_PAREN TOKEN_RIGHT_PAREN { 
            CustomFunction* func = findFunction(identi); 
            if (func != nullptr) {
                func->execute();
            } else {
                std::cerr << "Error: Function " << identi << " not defined." << std::endl;
            }
        }
        ;

%%

int yyerror(const char* s)
{
    printf("Parse error at line %d: %s\n", count_line, yytext);
    return 1;
}
