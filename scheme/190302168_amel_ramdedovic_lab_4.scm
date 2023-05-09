

; list-ref -> reference with 0 
; this will work with list up to 3 elemeents 
(define (function1 amel)

    (*(list-ref amel 1)(list-ref amel 0)(list-ref amel 2))

)


(define (fun1 n)

    (* car(fun1 n) car(cdr(fun1 n)))

)

(car '(1 2 3))

(car '(1 2 3))

(car