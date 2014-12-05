Attolisp
========

Small mindfree-form implementation of scheme-like language. For fun.

Now supports:
* numbers int/float, but strings very sporadic
* ariphmetic and logic
* function definitions
* recursion
* one-line expression repl

######Usage

$ python repl.py


```scheme
>> (define (len l) (if (eq (cdr l) None) 1 (plus 1 (len (cdr l)))))        
defined: len
>> (len (list 3 4 5))
3
```
