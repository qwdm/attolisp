import lexer


# test purposes
def log_args(funcname):
    import sys
    def decorator(func):
        def wrapper(*args, **kwargs):
            print >> sys.stderr, "%s args & kwargs: " % funcname
            if args: print >> sys.stderr, args
            if kwargs: print >> sys.stderr, kwargs 
            return func(*args, **kwargs)
        return wrapper
    return decorator
            

# global definitions scope
FUNCTIONS = {
    "plus" : (lambda x, y: x + y),
    "mult" : (lambda x, y: x * y),
    "gt"   : (lambda x, y: x > y),
    "eq"   : (lambda x, y: x == y),
    "neg"  : (lambda x: -x),
    "minus": (lambda x, y: x - y),
}


def expand(expr):
    """ expand expression with different rules for special """
    # atom
    if not isinstance(expr, list):
        return expr
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


if __name__ == '__main__':
    # simple test
    expressions = [
        ["mult", "4", "6"],
        ["define", ["square", "x"], ["mult", "x", "x"]],
        ["square", "6"],
        ["define", ["sum_squares", "x", "y"], ["plus", ["square", "x"], ["square", "y"]]],
        ["sum_squares", "3", "4"],
        ["define", ["pi"], ["3.14"]],
        ["define", ["circle_area", "r"], ["mult", ["square", "r"], ["pi"]]],
        ["circle_area", "4"],
    ]

    print dir()
    for expr in expressions:
        print calculate(expr)
