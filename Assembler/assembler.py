class Parser():
    def __init__(self, code):
        code_lines = code.strip()
        code_lines = code.split('\n')
        code_lines = [line.strip() for line in code_lines]

        self.code = []
        for line in code_lines:
            if line:
                if '//' in line:
                    continue
                self.code += [line]

        self.line_iterator = -1
        self.code_length = len(self.code)


    def has_more_lines(self):
        if self.line_iterator < self.code_length - 1:
            return True
    
    def advance(self):
        self.line_iterator += 1
    
    def instruction_type(self):
        curr = self.code[self.line_iterator]
        if curr[0] == '@':
            return "A"
        elif curr[0] == '(':
            return "L"
        else:
            return "C"

    def symbol(self):
        curr = self.code[self.line_iterator]
        if self.instruction_type() == "L":
            return curr[1:-1]
        elif self.instruction_type() == "A":
            return curr[1:]
    
    def dest(self):
        curr = self.code[self.line_iterator]
        if "=" in curr:
            curr = curr.split("=")
            return curr[0].strip()
        else:
            return None

    def comp(self):
        curr = self.code[self.line_iterator]
        if "=" in curr:
            curr = curr.split("=")
            if ";" in curr[1]:
                out = curr[1].split(";")[0]
                return out.strip()
            else:
                out = curr[1]
                return out.strip()
        else:
            if ";" in curr:
                out = curr.split(";")[0]
                return out.strip()
            else:
                out = curr
                return out.strip()
    
    def jump(self):
        curr = self.code[self.line_iterator]
        if ";" in curr:
            curr = curr.split(";")
            return curr[-1].strip() 
        else:
            return None
            


hack_assembly =   """
// x = 5+1
@5
D = A + 1
@x
M = D
"""

