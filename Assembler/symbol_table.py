class SymbolTable():
    def __init__(self):
        self.symbol_table = {"R0":0, "R1":1, "R2":2, "R3":3, 
                             "R4":4, "R5":5, "R6":6, "R7":7, 
                             "R8":8, "R9":9, "R10":10, "R11":11, 
                             "R12":12, "R13":13, "R14":14, "R15":15}
    
    def translate(self, symbol):
        if symbol in self.symbol_table:
            return self.symbol_table[symbol]
        else:
            val = len(self.symbol_table)
            self.symbol_table[symbol] = val
            return val
        