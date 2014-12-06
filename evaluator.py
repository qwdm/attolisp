import sys
import lexer

def log_args(funcname):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print >> sys.stderr, "%s args & kwargs: " % funcname
            if args: print >> sys.stderr, args
            if kwargs: print >> sys.stderr, kwargs 
            return func(*args, **kwargs)
        return wrapper
    return decorator


_ = staticmethod

class Scope:
    _add = _(lambda *A: reduce(lambda x, y: x + y, A))
    _mul = _(lambda *A: reduce(lambda x, y: x * y, A))
    _sub = _(lambda *A: (A[0] - A[1]) if len(A) == 2 else -A[0])
    _div = _(lambda x, y: x / y)
    _rem = _(lambda x, y: x % y)
    

    _eq  = _(lambda x, y: x == y)
    _gt  = _(lambda x, y: x > y)

    cons = _(lambda x, y: (x, y))
    car  = _(lambda pair: pair[0])
    cdr  = _(lambda pair: pair[1])
    list = _(lambda *A: None if not A else Scope.cons(A[0], Scope.list(*A[1:])))

    upcs = _(lambda x: x.upper())
    

#Scope.inc = _(lambda *A: eval("Scope._add(1, A[0])"))
#
#print Scope.inc(5)
#
#Scope.fact = _(lambda *A: eval("1 if Scope._eq(A[0], 0) else Scope._mul(A[0], Scope.fact(Scope._sub(A[0], 1)))"))
#
#print Scope.fact(5)


def define(name, params, expr):
    """ expr - list """
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
    """ take expr - list or atom,
        return expanded string
    """
    if not isinstance(expr, list):
        if expr in Scope.__dict__:
            return "Scope.%s" % expr
        else:
            return expr
    # special form if
    elif expr[0] == 'if':
        return "%s if %s else %s" % (expand(expr[2]), expand(expr[1]), expand(expr[3]))
    # common call function form
    else:
        return "%s(%s)" % (expand(expr[0]), ', '.join(map(expand, expr[1:]))) 


def calculate(expr):

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
