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

