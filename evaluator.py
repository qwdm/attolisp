##################################################33
# conservate this for the better future
#def mult(a, b): return a * b
#
#def mkfun(name):
#    return lambda lst: "(%s(%s))" % (name, ",".join(map(str,lst)))
#
#a = mkfun("mult")
#foo = a([2, 3])
#print eval(foo)
#
#
#foo = a(['x', 'y'])
#x, y = 4, 8
#print eval(foo)

####################################################

def plus(a, b): return "(%s + %s)" % (a, b)

FUNCTIONS = {
    "plus" : (lambda x, y: x + y),
    "mult" : (lambda x, y: x * y),
    "cond" : (lambda test, t_clause, f_clause: t_clause if test else f_clause),
    "gt"   : (lambda x, y: x > y),
    "eq"   : (lambda x, y: x == y),
    "neg"  : (lambda x: -x),
}


def expand(expr):
    if not isinstance(expr, list):
        return expr
    else:
        op = expr[0]
        params = expr[1:]
        return "(FUNCTIONS['%s'](%s))" % (expand(op), ",".join(map(expand, params)))


#print expand(['func', ['square','x'], 'y'])


def define(name, params, expr):
    if len(expr) == 1: #const
        string = 'lambda : %s' % expr[0]
    else:
        string = 'lambda %s: %s' % (','.join(params), expand(expr))
    print string
    FUNCTIONS[name] = eval(string)

#define("square", ["x"], ["mult", "x", "x"])
#
#print FUNCTIONS['square'](5)


def calculate(expr):
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
        print expr
        with open(expr[1]) as source:
            for line in source:
                calculate(line.rstrip())
                print line
                print FUNCTIONS
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
