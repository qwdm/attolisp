#!/usr/bin/env python
from lexer import makelist
from evaluator import calculate

# TODO multiline repl input

def makestring(result):
    if not isinstance(result, tuple):
        return str(result)
    else:
        reslist = []
        while result: # result => (1, (2, (3, None)))
            reslist.append(result[0])
            result = result[1]
        return "(%s)" % ' '.join(map(makestring, reslist))



if __name__ == "__main__":
    while True:
        line = raw_input(">> ").rstrip()
        if not line: 
            break
        result = calculate(makelist(line))
        print makestring(result)
