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
