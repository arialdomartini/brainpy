class Tape():
    def advance(self):
        pass

    def devance(self):
        pass

    def inc(self):
        print "performing a +"

    def dec(self):
        print "performing a -"

    def print_value(self):
        pass

    def read(self):
        pass

    def skip_forward(self):
        pass

    def skip_back(self):
        pass

    def nope(self):
        pass

    
def mainloop(program):
    tape = Tape()
    commands = {}
    commands[">"] = tape.advance
    commands["<"] = tape.devance
    commands["."] = tape.print_value
    commands["+"] = tape.inc
    commands["-"] = tape.dec
    commands["["] = tape.skip_forward
    commands["]"] = tape.skip_back
    commands["nope"] = tape.nope

    
    program_len = len(program)
    pc = 0

    while pc < program_len:
        input_value = program[pc]
        
        if input_value in commands.keys():
            cmd = commands[input_value]
        else:
            cmd = commands["nope"]

        cmd()
        pc += 1


mainloop("++--+")
