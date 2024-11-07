#include <vector>
#include <string>


class Command {
public:
    virtual ~Command() = default;
};


class CommandList : public Command {
private:
    std::vector<Command*> commands;  // Almacena la lista de comandos
public:
    void addCommand(Command* cmd) {
        commands.push_back(cmd);
    }

    const std::vector<Command*>& getCommands() const {
        return commands;
    }
};


class Move : public Command {
};

class TurnLeft : public Command {
};

class TurnRight : public Command {
};

class LightUp : public Command {
};

class Loop : public Command {
private:
    int iterations;
    CommandList* commands; 
public:
    Loop(int iter, CommandList* cmds) : iterations(iter), commands(cmds) {}

    int getIterations() const {
        return iterations;
    }

    CommandList* getCommands() const {
        return commands;
    }
};


class Procedure : public Command {
private:
    std::string name;
    CommandList* commands;
public:
    Procedure(const std::string& procName, CommandList* cmds) : name(procName), commands(cmds) {}

    const std::string& getName() const {
        return name;
    }

    CommandList* getCommands() const {
        return commands;
    }
};

class ProcedureCall : public Command {
private:
    std::string procedureName;
public:
    ProcedureCall(const std::string& name) : procedureName(name) {}

    const std::string& getProcedureName() const {
        return procedureName;
    }
};

