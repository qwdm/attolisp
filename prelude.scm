(define (abs n) (if (> n 0) n (neg n)))
(define (inc n) (+ n 1))
(define (dec n) (- n 1))

(define (empty? lst)
  (= lst None))

(define (map f l)
  (if (empty? l)
    None
    (cons (f (car l))
          (map f (cdr l)))))

(define (filter f lst)
  (if (empty? lst)
    None
    (if (f (car lst))
      (cons (car lst)
            (filter f (cdr lst)))
      (filter f (cdr lst)))))

(define (length lst)
  (if (empty? lst)
    0
    (+ 1
       (length (cdr lst)))))

(define (reverse lst)
  (if (= 1 (length lst))
    (list (car lst))
    (append (reverse (cdr lst))
            (list (car lst)))))

; reduce in python style with init (leftmost) value
(define (reduce f init lst)
  (if (empty? lst)
    init
    (reduce f
            (f init (car lst))
            (cdr lst))))

; (range a b) -> list from a to b inclusively
(define (range a b)
  (if (= a b)
    (list a)
    (cons a
          (range (inc a) b))))
