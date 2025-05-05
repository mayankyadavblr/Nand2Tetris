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
    
    def comp(self, computation):
        a0 = [0, 1, -1, 'D', 'A', '!D', '!A', '-D', '-A', 'D+1', 'A+1', 'D-1', 'A-1', 'D+A', 'D-A', 'A-D', 'D&A', 'D|A']
        a1 = [0, 0, 0, 0, 'M', 0, '!M', 0, '-M', 0, 'M+1', 0, 'M-1', 'D+M', 'D-M', 'M-D', 'D&M', 'D|M']

        
        if 'M' in computation:
            i = a1.index(computation)
            a = '1'
        else:
            i = a0.index(computation)
            a='0'
        
        out = "{0:b}".format(i)
        padding = 6 - len(out)
        return a + "0"*padding + out

