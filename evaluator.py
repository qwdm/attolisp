import lexer
from tests import log_args


            
#### BUILT-INS ####################################################

def _list(*args):
    """ builtin list function """
    if len(args) == 0:
        raise ValueError
    elif len(args) == 1:
        return (args[0], None)
    else:
        return (args[0], _list(*args[1:]))

# global definitions scope
FUNCTIONS = {
    # arithmetic
    "__plus__" : (lambda x, y: x + y),
    "__mult__" : (lambda x, y: x * y),
    "__minus__": (lambda x, y: x - y),
    "__div__"  : (lambda x, y: x / y), # py3 need another approach
    "__rem__"  : (lambda x, y: x % y),
    "__neg__"  : (lambda x: -x),

    # logical
    "__eq__"   : (lambda x, y: x == y),
    "__gt__"   : (lambda x, y: x > y),
    "__lt__"   : (lambda x, y: x < y),
    "__ge__"   : (lambda x, y: x >= y),
    "__le__"   : (lambda x, y: x <= y),

    # pairs
    "cons" : (lambda x, y: (x, y)),
    "car"  : (lambda x : x[0]),
    "cdr"  : (lambda x : x[1]),
    "list" : _list,
}



##############################################################

def expand(expr):
    """ expand expression with different rules for special """
    # atom
    if not isinstance(expr, list):
        return expr
#        if expr[0].isdigit(): # number
#            return expr
#        elif expr[0].isalpha(): # itendifier
#            return "(FUNCTIONS['%s']())" % expr
    # conditional if
    elif expr[0] == 'if':
        return "(%s if %s else %s)" % (expand(expr[2]), expand(expr[1]), expand(expr[3]))
    # logical and, or
    elif expr[0] == 'and' or expr[0] == 'or':
        return "(%s)" % (" %s " % expr[0]).join([expand(e) for e in expr[1:]])
    else:
        op = expr[0]
        params = expr[1:]
        return "(FUNCTIONS['%s'](%s))" % (expand(op), ",".join(map(expand, params)))



#@log_args('define')
def define(name, params, expr):
    if len(expr) == 1: #const
        string = 'lambda : %s' % expr[0]
    else:
        string = 'lambda %s: %s' % (','.join(params), expand(expr))
    FUNCTIONS[name] = eval(string)


#@log_args('calculate')
def calculate(expr):
    """ expr - python list of atoms and lists """
    # atom
    if not isinstance(expr, list):
        return expr
    # special forms: define
    elif expr[0] == 'define':
        name = expr[1][0]
        params = expr[1][1:]
        expr = expr[2]
        define(name, params, expr)
        return "defined: %s" % name 
    # special forms: require
    elif expr[0] == 'require':
        with open(expr[1]) as source:
            for line in source:
                if len(line) > 2:
                    calculate(lexer.makelist(line.rstrip()))
    # common expression
    else:
        return eval(expand(expr))
