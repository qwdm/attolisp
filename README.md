Attolisp
========

Small mindfree-form implementation of scheme-like language. For fun.

Now supports:
* numbers int/float, but strings very sporadic
* ariphmetic and logic
* function definitions
* first class functions
* recursion
* module import, multiline module definitions
* one-line expression repl

######Usage

$ python repl.py


```scheme
>> (> 4 5)
False
>> (+ 10 3)
13
>> (+ (upcs 'pussy') (upcs 'cat'))
PUSSYCAT
>> (require prelude.scm)  ; import definitions from module
defined: abs
defined: inc
....
defined: empty_qqq  ; empty? mangled into empty_qqq
>> (abs -5)
5
>> (define (length lst) (if (empty? lst) 0 (+ 1 (length (cdr lst)))))
defined: length
>> (length (list 6 4 5))
3
>> (map inc (list 1 2 3 4))
(2 3 4 5)
>> (define (fact n) (reduce * 1 (range 1 n)))
defined: fact
>> (fact 5)
120
```

also see examples in prelude.scm
