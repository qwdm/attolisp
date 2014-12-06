import sys
import evaluator
#from evaluator import Scope

def log_args(funcname):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print >> sys.stderr, "%s args & kwargs: " % funcname
            if args: print >> sys.stderr, args
            if kwargs: print >> sys.stderr, kwargs 
            return func(*args, **kwargs)
        return wrapper
    return decorator


def simple_calc_test():
    expressions = [
        ["__mult__", "4", "6"],
        ["define", ["square", "x"], ["__mult__", "x", "x"]],
        ["square", "6"],
        ["define", ["sum_squares", "x", "y"], ["__plus__", ["square", "x"], ["square", "y"]]],
        ["sum_squares", "3", "4"],
        ["define", ["pi"], ["3.14"]],
        ["define", ["circle_area", "r"], ["__mult__", ["square", "r"], ["pi"]]],
        ["circle_area", "4"],
    ]

    for expr in expressions:
        print evaluator.calculate(expr)

def expand_test():
    exprs = [
        "5",
        ["_plus", "5", "6"],
        ["_mult", ["_plus", "1", "2"], ["_plus", "3", "4"]],
    ]
    for e in exprs:
        print evaluator.expand(e)

if __name__ == "__main__":
#    print Scope.__dict__
    expand_test()

# TODO
##print deep_substitute('x', '0', ['+', ['*', 'x', 'y'], ['*', 'x', 'z']])
#define('foo', ['x', 'y'], ['_add', ['_mul', 'x', 'x'], ['_mul', 'y', 'y']])
##print Scope.__dict__
#print Scope.foo(3, 4)
#print eval("Scope.foo(3, 4)")
#
#print expand(['if', ['_gt', 'x', 'y'], 'x', 'y'])
#
#define('max', ['x', 'y'], ['if', ['_gt', 'x', 'y'], 'x', 'y'])
#define('inc', ['n'], ['_add', 'n', '1'])
#define('fac', ['n'], ['if', ['_eq', 'n', '0'], 
#                            '1', 
#                            ['_mul', 'n', 
#                                     ['fac', ['_sub', 'n', '1']]]])
#define('foo', ['f', 'x'], ['f', ['f', 'x']])
#
#
#print Scope.max(3,4)
#print Scope.inc(17)
#print Scope.fac(5)
#print Scope.foo(Scope.inc, 4)
#print eval(expand(['foo', 'inc', '4']))
