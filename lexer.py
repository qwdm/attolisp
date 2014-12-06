""" perform lexical analysys """
import re

BIGNUM = 1000

def makelist(string):
    """ make python list from input string """ 
    # change ariphmetic operators to builtin words
#    pre = r'\(\s*' # only if open paren. -> only if operator
#    presub = r'('
    post = r'([^\w])'
    postsub = r'\1'
    ariphmetic_subs = [
            (r'\+', '_add'),
            (r'-', '_sub'),
            (r'\*', '_mul'),
            (r'/', '_div'),
            (r'%', '_rem'),
            (r'>=', '_ge'),
            (r'<=', '_le'),
            (r'=', '_eq'),
            (r'>', '_gt'),
            (r'<', '_lt'),
    ]
    ariphmetic_subs = [(s[0]+post, s[1]+postsub) for s in ariphmetic_subs]

    # parens -> brackets
    python_syntax_sub = [
            (r'\(', r'['),
            (r'\)', r']'),
    ]

    # identifiers and put into " "
    python_syntax_sub += [(r'([-\w.?]+)',r'"\1"')]

    # ? -> _qqq and - -> ___
    python_syntax_sub += [(r'\?', r'_qqq'),
                          (r'(\w)-(\w)', r'\1___\2')]

    # commas between elements in lists
    python_syntax_sub += [(r'(\s+)',r', ')]

    ##### perform substitute
    subs = ariphmetic_subs + python_syntax_sub
    for s in subs:
        string = re.sub(s[0], s[1], string, BIGNUM)

    # return evaluated as python list
    print string
    return eval(string)
