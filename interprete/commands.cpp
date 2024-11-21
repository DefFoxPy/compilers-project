#include <commands.hpp>
#include <iostream>
#include <fstream>

extern std::ofstream output_file;

Command::~Command() {}

CommandList::~CommandList() {
    for (auto cmd : commands) {
        delete cmd; // Liberar memoria de cada comando
    }
}

void CommandList::destroy() noexcept {}

void CommandList::addCommand(Command* cmd) {
    commands.push_back(cmd);
}

void CommandList::execute() noexcept {
    for (auto cmd : commands) {
        cmd->execute(); 
    }
}

void Move::execute() noexcept {
    std::cout << "Move forward" << std::endl;
    output_file << "Move forward" << std::endl;
}


void TurnLeft::execute() noexcept {
    std::cout << "Turn left" << std::endl;
    output_file << "Turn left" << std::endl;

}


void TurnRight::execute() noexcept {
    std::cout << "Turn right" << std::endl;
    output_file << "Turn right" << std::endl;
}


void LightUp::execute() noexcept {
    std::cout << "Light up the tile" << std::endl;
    output_file << "Light up the tile" << std::endl;
}


Loop::Loop(int iterations, CommandList* commands)
    : iterations(iterations), commands(commands) {}

Loop::~Loop() {
    delete commands; 
}

void Loop::execute() noexcept {
    for (int i = 0; i < iterations; ++i) {
        //std::cout << "Loop iteration: " << i + 1 << std::endl;
        commands->execute(); 
    }
}

CustomFunction::CustomFunction(const std::string& name, CommandList* commands)
    : name(name), commands(commands) {}

void CustomFunction::execute() noexcept {
    std::cout << "Executing function: " << name << std::endl;
    commands->execute();
}

std::string CustomFunction::getName() const {
    return name;
}

CustomFunction::~CustomFunction() {
    delete commands; 
}

Procedure::Procedure(const std::string& name, CommandList* commands)
    : name(name), commands(commands) {}

Procedure::~Procedure() {
    delete commands; 
}

void Procedure::execute() noexcept {
    std::cout << "Executing procedure: " << name << std::endl;
    commands->execute();
}
