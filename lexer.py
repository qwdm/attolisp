""" perform lexical analysys """
import re

def makelist(string):
    string = re.sub(r'\(',r'[', string, 400)
    string = re.sub(r'\)',r']', string, 400)
    string = re.sub(r'(-*[\w.]+)',r'"\1"', string, 400)
    string = re.sub(r'(\s+)',r', ', string, 400)
    return eval(string)
