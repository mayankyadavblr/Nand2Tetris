from parser import Parser 
from translator import Translator

class Assembler():
    def __init__(self, code):
        self.parser = Parser(code)
        self.translator = Translator()
        self.assembly = ""
    
    def main(self):
        while self.parser.has_more_lines():
            self.parser.advance()
            instruction = self.parser.instruction_type()
            if instruction == 'A':
                symbol = self.parser.symbol()
                self.assembly += "0" + symbol + "\n"
            elif instruction == 'C':
                comp = self.parser.comp()
                comp = self.translator.comp(comp)

                dest = self.parser.dest()
                dest = self.translator.dest(dest)

                jump = self.parser.jump()
                jump = self.translator.jump(jump)

                self.assembly += "111" + comp + dest + jump + "\n"
            elif instruction == 'L':
                symbol = self.parser.symbol()
        
        return self.assembly



hack_assembly =   """
// x = 5+1
@5
D=A+1
(LOOP)
@x
M=D;JGT
"""
assembler = Assembler(hack_assembly)
assembler.main()
print(assembler.assembly)
print(assembler.parser.symbol_table.symbol_table)

