#include <vector>
#include <string>
#include <iostream>


class Command {
public:
    virtual ~Command() = default;
    virtual void execute() = 0;
};


class CommandList : public Command {
private:
    std::vector<Command*> commands;  // Almacena la lista de comandos
public:
    virtual ~CommandList();
    void addCommand(Command* cmd);
    void execute();
};


class Move : public Command {
public:  
    void execute() override;
};

class TurnLeft : public Command {
public:  
    void execute() override;
};

class TurnRight : public Command {
public:  
    void execute() override;
};

class LightUp : public Command {
public:  
    void execute() override;
};

class Loop : public Command {
private:
    int iterations;
    CommandList* commands; 
public:
    Loop(int iter, CommandList* cmds); 
    virtual ~Loop(); 
    void execute() override;
};


class Procedure : public Command {
private:
    std::string name;
    CommandList* commands;
public:  
    Procedure(const std::string& procName, CommandList* cmds);
    virtual ~Procedure(); 
    void execute() override; 
};

class ProcedureCall : public Command {
private:
    std::string procedureName;
public:
    ProcedureCall(const std::string& name);
    void execute() override;
};

