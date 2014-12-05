import sys
import evaluator

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
