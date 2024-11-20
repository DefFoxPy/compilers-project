#include <stdio.h>
#include <stdlib.h>
#include <fstream>
#include <commands.hpp>


extern FILE* yyin;
extern int yyparse();
extern Command* parser_result;

std::ofstream output_file;

void usage(char* argv[])
{
    printf("Usage: %s input_file\n", argv[0]);
    exit(1);
}

int main(int argc, char* argv[])
{
    if (argc != 2)
    {
        usage(argv);
    }

    yyin = fopen(argv[1], "r");

    if (!yyin)
    {
        printf("Could not open %s\n", argv[1]);
        exit(1);
    }

    output_file.open("action.txt");

    if (!output_file.is_open())
    {
        printf("Could not create output.txt\n");
        exit(1);
    }
    int result = yyparse();

    if (result == 0)
    {
        printf("Parse successful!\n");
        parser_result->execute();
        parser_result->destroy();
        printf("\n\nMemoria liberada...\n");
    }
    else
    {
        printf("Parse failed!\n");
    }
    output_file.close();
    return 0;
}