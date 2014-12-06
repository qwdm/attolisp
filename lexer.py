""" perform lexical analysys """
import re

BIGNUM = 1000

def makelist(string):
    """ make python list from input string """ 
    # change ariphmetic operators to builtin words
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


def splitfile(fileobj):
    lines = fileobj.readlines()
    # take off comments
    lines = [line.rstrip() for line in lines if not line.startswith(';') or len(line) < 2]
    strings = []
    s = ''
    for line in lines:
        if line.startswith('('):
            strings.append(s)
            s = line
        else:
            s += line
    strings.append(s)  
    strings = strings[1:]
    return strings
