from lexer import makelist
from evaluator import calculate
#from NEW import calculate

if __name__ == "__main__":
    while True:
        line = raw_input(">> ").rstrip()
        if not line: 
            break
        print calculate(makelist(line))
