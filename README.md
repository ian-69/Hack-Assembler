# Hack-Assembler

Hey Everyone I've made a Simple and functional Assembler using Python, I've attached the source code.

This is a Python code that implements an assembler for the Hack assembly language, which is a simple assembly language used in the Nand2Tetris course. The code consists of four main classes: Parser, Code, SymbolTable, and Pass.

Parser Class: The Parser class is responsible for parsing a single assembly language instruction. It takes an instruction as input and extracts its components, such as the type of instruction (A, L, or C), the value, destination, computation, and jump parts.

Code Class: The Code class is responsible for translating a computation or jump part of an instruction into binary code. It takes a term as input and returns the corresponding binary code.

The SymbolTable: class is responsible for managing a symbol table that maps symbols (labels) to their corresponding addresses. It provides methods to add predefined symbols, check if a symbol exists, add a new symbol, and get the address of a symbol.

Pass Class: The Pass class is responsible for performing two passes over the assembly language code:

First Pass: The first pass goes through the code and adds labels to the symbol table.

Second Pass: The second pass goes through the code again and translates each instruction into binary code using the Parser and Code classes. The resulting binary code is written to a .hack file.

Main Function: The main function creates a SymbolTable instance and a Pass instance, and then calls the firstPass and secondPass methods of the Pass instance to assemble the code.


Here's a high-level overview of the assembly process:

The first pass reads the assembly language code and adds labels to the symbol table.

The second pass reads the assembly language code again and translates each instruction into binary code using the Parser and Code classes.

The resulting binary code is written to a .hack file.



I hope this helps
