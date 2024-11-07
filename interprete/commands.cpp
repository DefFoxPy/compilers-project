#include <commands.hpp>
#include <iostream>

CommandList::~CommandList() {
    for (auto cmd : commands) {
        delete cmd; // Liberar memoria de cada comando
    }
}

void CommandList::addCommand(Command* cmd) {
    commands.push_back(cmd);
}

void CommandList::execute() {
    for (auto cmd : commands) {
        cmd->execute(); 
    }
}


void Move::execute() {
    std::cout << "Move forward" << std::endl;
}


void TurnLeft::execute() {
    std::cout << "Turn left" << std::endl;
}


void TurnRight::execute() {
    std::cout << "Turn right" << std::endl;
}


void LightUp::execute() {
    std::cout << "Light up the tile" << std::endl;
}


Loop::Loop(int iterations, CommandList* commands)
    : iterations(iterations), commands(commands) {}

Loop::~Loop() {
    delete commands; 
}

void Loop::execute() {
    for (int i = 0; i < iterations; ++i) {
        std::cout << "Loop iteration: " << i + 1 << std::endl;
        commands->execute(); 
    }
}


Procedure::Procedure(const std::string& name, CommandList* commands)
    : name(name), commands(commands) {}

Procedure::~Procedure() {
    delete commands; 
}

void Procedure::execute() {
    std::cout << "Executing procedure: " << name << std::endl;
    commands->execute();
}


ProcedureCall::ProcedureCall(const std::string& name)
    : procedureName(name) {}

void ProcedureCall::execute() {
    std::cout << "Calling procedure: " << procedureName << std::endl;
}
