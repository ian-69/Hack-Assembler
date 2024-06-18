#!/usr/bin/env python3

import sys

class Parser:
    """
    The Parser class is used to parse assembly instructions.
    """
    def __init__(self, inst):
        self.inst = inst  # the assembly instruction
        self.type = None  # the type of the instruction ('A', 'C', or 'L')
        self.valueV = None  # the value part of an A-instruction
        self.destV = None  # the destination part of a C-instruction
        self.compV = None  # the computation part of a C-instruction
        self.jumpV = None  # the jump part of a C-instruction
        self.cleanUp()  # clean up the instruction by removing whitespace and comments
        self.checkType()  # determine the type of the instruction

    def checkType(self):
        """
        Determine the type of the instruction based on its first character.
        """
        if self.inst == '':
            return 
        elif self.inst.startswith('@'):
            self.type = 'A'  # A-instruction
        elif self.inst.startswith('('):
            self.type = 'L'  # Label
        else:
            self.type = 'C'  # C-instruction

    def value(self):
        """
        Extract the value from an A-instruction.
        """
        if self.type != 'A':
            return None
        self.valueV = self.inst[1:].split(' ')[0]
        return self.valueV

    def cleanUp(self):
        """
        Remove whitespace and comments from the instruction.
        """
        self.inst = self.inst.strip()
        cInd = self.inst.find('//')
        if cInd == -1:
            self.inst = self.inst.strip()
        elif cInd == 0:
            self.inst = ''
        else:
            self.inst = self.inst[0:cInd].strip()

    def dest(self):
        """
        Extract the destination part of a C-instruction.
        """
        eInd = self.inst.find('=')
        if self.type != 'C' or eInd == -1:
            return None
        self.destV = self.inst[0:eInd].strip()
        return self.destV

    def comp(self):
        """
        Extract the computation part of a C-instruction.
        """
        eInd = self.inst.find('=')
        sInd = self.inst.find(';')
        if self.type != 'C':
            return None
        if eInd != -1 and sInd != -1:
            self.compV = self.inst[eInd+1:sInd].strip()
        elif eInd != -1 and sInd == -1:
            self.compV = self.inst[eInd+1:].strip()
        elif eInd == -1 and sInd != -1:
            self.compV = self.inst[0:sInd].strip()
        elif eInd == -1 and sInd == -1:
            self.compV = self.inst.strip()
        return self.compV

    def jump(self):
        """
        Extract the jump part of a C-instruction.
        """
        sInd = self.inst.find(';')
        if self.type != 'C' or sInd == -1:
            return None
        self.jumpV = self.inst[sInd+1:].strip()
        return self.jumpV

class Code:
    """
    The Code class is used to convert parts of instructions to their binary representations.
    """
    def __init__(self, term):
        self.term = term  # the term to convert
        self.valueB = None  # the binary value of the term
        self.destB = None  # the binary destination
        self.jumpB = None  # the binary jump
        self.compB = None  # the binary computation

    def decimalToBinary(self, n):
        """
        Convert a decimal number to a 16-bit binary string.
        """
        return format(n, '016b')

    def value(self):
        """
        Convert the value of an A-instruction to binary.
        """
        if self.term is None:
            return None
        self.valueB = self.decimalToBinary(int(self.term))
        return self.valueB

    def dest(self):
        """
        Convert the destination part of a C-instruction to binary.
        """
        if self.term is None:
            self.destB = '000'
        elif self.term == 'M':
            self.destB = '001'
        elif self.term == 'D':
            self.destB = '010'
        elif self.term == 'MD':
            self.destB = '011'
        elif self.term == 'A':
            self.destB = '100'
        elif self.term == 'AM':
            self.destB = '101'
        elif self.term == 'AD':
            self.destB = '110'
        elif self.term == 'AMD':
            self.destB = '111'
        return self.destB

    def comp(self):
        """
        Convert the computation part of a C-instruction to binary.
        """
        a = '0'
        c = ''
        if self.term is None:
            self.compB = None
        elif self.term == '0':
            a = '0'
            c = '101010'
        elif self.term == '1':
            a = '0'
            c = '111111'
        elif self.term == '-1':
            a = '0'
            c = '111010'
        elif self.term == 'D':
            a = '0'
            c = '001100'
        elif self.term == 'A':
            a = '0'
            c = '110000'
        elif self.term == '!D':
            a = '0'
            c = '001101'
        elif self.term == '!A':
            a = '0'
            c = '110001'
        elif self.term == '-D':
            a = '0'
            c = '001111'
        elif self.term == '-A':
            a = '0'
            c = '110011'
        elif self.term == 'D+1':
            a = '0'
            c = '011111'
        elif self.term == 'A+1':
            a = '0'
            c = '110111'
        elif self.term == 'D-1':
            a = '0'
            c = '001110'
        elif self.term == 'A-1':
            a = '0'
            c = '110010'
        elif self.term == 'D+A':
            a = '0'
            c = '000010'
        elif self.term == 'D-A':
            a = '0'
            c = '010011'
        elif self.term == 'A-D':
            a = '0'
            c = '000111'
        elif self.term == 'D&A':
            a = '0'
            c = '000000'
        elif self.term == 'D|A':
            a = '0'
            c = '010101'
        elif self.term == 'M':
            a = '1'
            c = '110000'
        elif self.term == '!M':
            a = '1'
            c = '110001'
        elif self.term == '-M':
            a = '1'
            c = '110011'
        elif self.term == 'M+1':
            a = '1'
            c = '110111'
        elif self.term == 'M-1':
            a = '1'
            c = '110010'
        elif self.term == 'D+M':
            a = '1'
            c = '000010'
        elif self.term == 'D-M':
            a = '1'
            c = '010011'
        elif self.term == 'M-D':
            a = '1'
            c = '000111'
        elif self.term == 'D&M':
            a = '1'
            c = '000000'
        elif self.term == 'D|M':
            a = '1'
            c = '010101'
        self.compB = a + c
        return self.compB

    def jump(self):
        """
        Convert the jump part of a C-instruction to binary.
        """
        if self.term is None:
            self.jumpB = '000'
        elif self.term == 'JGT':
            self.jumpB = '001'
        elif self.term == 'JEQ':
            self.jumpB = '010'
        elif self.term == 'JGE':
            self.jumpB = '011'
        elif self.term == 'JLT':
            self.jumpB = '100'
        elif self.term == 'JNE':
            self.jumpB = '101'
        elif self.term == 'JLE':
            self.jumpB = '110'
        elif self.term == 'JMP':
            self.jumpB = '111'
        return self.jumpB

class SymbolTable:
    """
    The SymbolTable class stores and manages symbols and their associated values.
    """
    def __init__(self):
        self.symbols = {}  # dictionary to store symbols and their values
        self.addPreDef()  # add predefined symbols

    def addPreDef(self):
        """
        Add predefined symbols to the symbol table.
        """
        for i in range(16):
            self.symbols["R"+str(i)] = i
        self.symbols["SCREEN"] = 16384
        self.symbols["KBD"] = 24576
        self.symbols["SP"] = 0
        self.symbols["LCL"] = 1
        self.symbols["ARG"] = 2
        self.symbols["THIS"] = 3
        self.symbols["THAT"] = 4

    def exists(self, symbol):
        """
        Check if a symbol exists in the table.
        """
        return self.symbols.get(symbol) is not None

    def addSym(self, symbol, value):
        """
        Add a new symbol to the table.
        """
        self.symbols[symbol] = value

    def getVal(self, symbol):
        """
        Get the value of a symbol.
        """
        return self.symbols.get(symbol)

class Passs:
    """
    The Passs class performs the first and second pass over the assembly code.
    """
    def __init__(self, symTab):
        self.symTab = symTab  # the symbol table

    def firstPass(self):
        """
        First pass: record the memory address of labels.
        """
        with open(sys.argv[1], 'r') as asm:
            lineNo = -1
            for inst in asm:
                p = Parser(inst)
                if p.type == 'A' or p.type == 'C':
                    lineNo += 1
                if p.type == 'L':
                    symbol = p.inst[1:-1]
                    if not self.symTab.exists(symbol):
                        self.symTab.addSym(symbol, lineNo + 1)

    def secPass(self):
        """
        Second pass: translate instructions into binary code.
        """
        with open(sys.argv[1].split('.')[0] + '.hack', 'w') as hack:
            with open(sys.argv[1], 'r') as asm:
                n = 16
                for inst in asm:
                    p = Parser(inst)
                    if p.type == 'A':
                        symbol = p.inst[1:]
                        if self.symTab.exists(symbol):
                            c = Code(self.symTab.getVal(symbol))
                            hack.write(c.value() + '\n')
                        else:
                            try:
                                val = int(symbol)
                                c = Code(val)
                                hack.write(c.value() + '\n')
                            except ValueError:
                                self.symTab.addSym(symbol, n)
                                c = Code(n)
                                hack.write(c.value() + '\n')
                                n += 1
                    elif p.type == 'C':
                        d = Code(p.dest())
                        c = Code(p.comp())
                        j = Code(p.jump())
                        hack.write('111' + c.comp() + d.dest() + j.jump() + '\n')

def main():
    """
    The main function initializes the symbol table and performs both passes.
    """
    st = SymbolTable()
    pas = Passs(st)
    pas.firstPass()
    pas.secPass()

if __name__ == "__main__":
    main()
