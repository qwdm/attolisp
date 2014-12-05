""" perform lexical analysys """
import re

BIGNUM = 1000

def makelist(string):
    """ make python list from input string """ 
    # change ariphmetic operators to builtin words
    pre = r'\(\s*' # only if open paren. -> only if operator
    presub = r'('
    ariphmetic_subs = [
            (r'\+', '__plus__'),
            (r'-', '__minus__'),
            (r'\*', '__mult__'),
            (r'/', '__div__'),
            (r'%', '__rem__'),
            (r'=', '__eq__'),
            (r'> ', '__gt__'),
            (r'< ', '__lt__'),
            (r'>=', '__ge__'),
            (r'<=', '__le__'),
    ]
    ariphmetic_subs = [(pre+s[0], presub+s[1]) for s in ariphmetic_subs]

    # parens -> brackets
    python_syntax_sub = [
            (r'\(', r'['),
            (r'\)', r']'),
    ]

    # identifiers and put into " "
    python_syntax_sub += [(r'(-*[\w.]+)',r'"\1"')]

    # commas between elements in lists
    python_syntax_sub += [(r'(\s+)',r', ')]

    ##### perform substitute
    subs = ariphmetic_subs + python_syntax_sub
    for s in subs:
        string = re.sub(s[0], s[1], string, BIGNUM)

    # return evaluated as python list
    return eval(string)
