class Translator():
    
    def dest(self, destination):
        labels = [None, 'M', 'D', 'DM', 'A', 'AM', 'AD', 'ADM']
        i = labels.index(destination)
        out = "{0:b}".format(i)
        padding = 3 - len(out)
        return "0"*padding + out

    def jump(self, jump_instr):
        labels = [None, 'JGT', 'JEQ', 'JGE', 'JLT', 'JNE', 'JLE', 'JMP']
        i = labels.index(jump_instr)
        out = "{0:b}".format(i)
        padding = 3 - len(out)
        return "0"*padding + out

translator = Translator()
print(translator.jump("JLT"))
