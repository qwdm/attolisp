# polish calc a.k.a lispcalc                             

#######################
def plus(*args):
    return sum(args)

def minus(a, b):
    return a - b

def multiply(*args):
    return reduce(lambda a,b: a*b, args)

def div(a, b):
    return a / b

def reminder(a, b):
    return a % b

BUILTIN = { 
        "+" : plus,
        "-" : minus,
        "*" : multiply,
        "/" : div,
        "%" : reminder
}

FUNCTIONS = {}


class expr(object):
    def __init__(self, exprlist):
#        self.op = self.calc(exprlist[0])
#        self.args = [self.calc(e) for e in exprlist[1:]]
        if isinstance(exprlist, list):
            self.op = exprlist[0]
            self.args = exprlist[1:]
            self.compound = True
        else: # atom
            self.compound = False
            self.value = exprlist

    def calc(self):
        if not self.compound:
            return self.value
        
        if self.op == "define":
            func_name = 


        if self.op in BUILTIN:
            args = [expr(arg).calc() for arg in self.args]
            return BUILTIN[self.op](*args)


class Function(object):
    def __init__(self, name, formal_params, expr):


a = ["+", ["-", 10, 9], 5, 6]
print expr(a).calc()


#>>> a = eval("lambda %s: %s" % ("x, y, z", "sum([x, y, z])"))
#>>> a(5,6,7)
#18
#>>> x = 5
#>>> a = eval("lambda %s: %s" % ("y", "x + y"))
#>>> a(3)
#8
#>>> a = eval("lambda %s: %s" % ("y", "x + y"))

