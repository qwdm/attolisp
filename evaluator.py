import sys
import lexer
#from tests import log_args

_ = staticmethod


####### built-ins ##########

def _append(a, b):
    """ append 2 linked lists """
    _a, _b = [], []
    while a:
        _a.append(a[0])
        a = a[1]
    while b:
        _b.append(b[0])
        b = b[1]
    _ab = _a + _b
    ab = None
    while _ab:
        ab = (_ab.pop(), ab)
    return ab


class Scope: # global scope

    # ariphmetic
    _add = _(lambda *A: reduce(lambda x, y: x + y, A))
    _mul = _(lambda *A: reduce(lambda x, y: x * y, A))
    _sub = _(lambda *A: (A[0] - A[1]) if len(A) == 2 else -A[0])
    _div = _(lambda x, y: x / y)
    _rem = _(lambda x, y: x % y)
    
    # comparisons
    _eq  = _(lambda x, y: x == y)
    _gt  = _(lambda x, y: x > y)
    _ge  = _(lambda x, y: x >= y)
    _lt  = _(lambda x, y: x < y)
    _le  = _(lambda x, y: x <= y)

    # pairs, lists
    cons = _(lambda x, y: (x, y))
    car  = _(lambda pair: pair[0])
    cdr  = _(lambda pair: pair[1])
    list = _(lambda *A: None if not A else Scope.cons(A[0], Scope.list(*A[1:])))
    pair_qqq = _(lambda x: isinstance(x, tuple))
    append = _(_append)

    #strings
    upcs = _(lambda x: x.upper())



def define(name, params, expr):
    """ Add definition in global scope
        take expr : list
        return None
    """
    Scope.__dict__[name] = None # add name in scope for correct expanding

    def deep_substitute(par, index, expr):
        if not isinstance(expr, list):
            if expr == par:
                return "A[%s]" % index
            else:
                return expr
        else:
            return [deep_substitute(par, index, e) for e in expr]

    for i, p in enumerate(params):
        expr = deep_substitute(p, i, expr)
    
    Scope.__dict__[name] = _(lambda *A: eval(expand(expr)))


#@log_args('expand')
def expand(expr):
    """ Expand expression into string for evaluating
        take expr - list or atom
        return expanded string
    """
    # atom / identificator
    if not isinstance(expr, list):
        if expr in Scope.__dict__:
            return "Scope.%s" % expr
        else:
            return expr

    # special form if
    elif expr[0] == 'if':
        return "(%s if %s else %s)" % (expand(expr[2]), expand(expr[1]), expand(expr[3]))

    # special form and, or
    elif expr[0] == 'and' or expr[0] == 'or':
        return "(%s)" % ((' %s ' % expr[0]).join(map(expand, expr[1:])))

    # common call function form
    else:
        return "(%s)(%s)" % (expand(expr[0]), ', '.join(map(expand, expr[1:])))


def calculate(expr):
    """ Calculate expression list """

    # atom
    if not isinstance(expr, list):
        return eval(expand(expr))

    # define function
    elif expr[0] == 'define':
        name = expr[1][0]
        params = expr[1][1:]
        expr = expr[2]
        define(name, params, expr)
        return "defined: %s" % name
    
    # require module
    elif expr[0] == 'require':
        defined = []
        with open(expr[1]) as source:
            for expr in lexer.splitfile(source):
                defined.append(calculate(lexer.makelist(expr)))
        return '\n'.join(defined)

    # common expression
    else:
        return eval(expand(expr))
