#include <vector>
#include <string>
#include <iostream>


class Command {
public:
    virtual ~Command();
    virtual void destroy() noexcept = 0;//**
    virtual void execute() noexcept = 0;
};


class CommandList : public Command {
private:
    std::vector<Command*> commands;  // Almacena la lista de comandos
public:
    virtual ~CommandList();
    void destroy() noexcept override;
    void addCommand(Command* cmd);
    void execute() noexcept override;
};


class Move : public Command {
public:  
    void execute() noexcept override;
    void destroy() noexcept override {
        delete this;
    }
};

class TurnLeft : public Command {
public:  
    void execute() noexcept override;
    void destroy() noexcept override {
        delete this;
    }
};

class TurnRight : public Command {
public:  
    void execute() noexcept override;
    void destroy() noexcept override {
        delete this;
    }
};

class LightUp : public Command {
public:  
    void execute() noexcept override;
    void destroy() noexcept override {
        delete this;
    }
};

class Loop : public Command {
private:
    int iterations;
    CommandList* commands; 
public:
    Loop(int iter, CommandList* cmds); 
    virtual ~Loop(); 
    void execute() noexcept override;
    void destroy() noexcept override {
        delete this;
    }
};


class Procedure : public Command {
private:
    std::string name;
    CommandList* commands;
public:  
    Procedure(const std::string& procName, CommandList* cmds);
    virtual ~Procedure(); 
    void execute() noexcept override;
    void destroy() noexcept override {
        delete this;
    }
};

class ProcedureCall : public Command {
private:
    std::string procedureName;
public:
    ProcedureCall(const std::string& name);
    void execute() noexcept override;
    void destroy() noexcept override {
        delete this;
    }
};

