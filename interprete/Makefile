CXX = g++
FLEX = flex
BISON = bison -Wall --defines=token.h #Tuve que eliminar -Wcounterexamples con windows no me corria

all: interpreter

interpreter: parser.o scanner.o main.o commands.o
	$(CXX) scanner.o parser.o main.o commands.o -o interpreter

parser.o: parser.c
	$(CXX) -c -I. parser.c

parser.c: parser.bison
	$(BISON) -v --output parser.c parser.bison

scanner.o: token.h scanner.c
	$(CXX) -c scanner.c

scanner.c: scanner.flex
	$(FLEX) -o scanner.c scanner.flex

main.o: token.h main.c
	$(CXX) -c -I. main.c

commands.o: commands.hpp commands.cpp
	$(CXX) -c -I. commands.cpp

.PHONY:
clean:
	$(RM) *.o parser.c parser.output token.h scanner.c interpreter output.txt