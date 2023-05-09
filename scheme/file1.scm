
(define (square x) (* x x ))
(display (square 5))

(define (c a b) (sqrt(+ (square a) (square b )))) 
(display (c 3 4)) 


(define (fact n) 
    (if (= n 0)
        1 
        (* n (fact(- n 1))))
)
(display (fact 10))

(newline)

(define (compare x y)
    (cond 
        ((> x y) "This is returned")
        ((< x y) "It is false")
        (else "They are equal")
    )
)

(display (compare 10 2))


(define (leap x) 
    (cond 
    
        (zero? (modulo x 400) "Leap")
        (zero? (modulo x 100) "NOT leap")
        (zero? (modulo x 4) "A leap year")
        (else "It is not leap")
    
    )


;------------------------This one works -------------------
(define (leap x )
    (cond 
    
        ((zero? (modulo x 400)) "Leap")
        ((zero? (modulo x 100)) "NOT leap")
        ((zero? (modulo x 4)) "A leap year")
        (else "It is not leap")
    )
)

(display (leap 1204))
;----------------------------------------------------------


(newline)
(define pointer1 '(1 2 3))
(display pointer1)
)
; append -> combines in one lis (A B ) (C D) (A B C D )
; const -> (A B) (C D) ((A B) C D)

(define (merge x list1) 
    (cons x list1)

)

display(merge '(10 20) '(30 40))

(define (merge x list1) 
    (append x list1)

)

display(merge '(10 20) '(30 40))



(define (factorail n) (* n n ))
(display (fact 5))


(define (fact1 n) (+ n n))


(display "Enter the number : ")
(define (fact1 n)

    (if(= n 0) 
        1
    (* n (fact1 (- n 1)))
    
    )
)
(display "Enter the number : ")
(define n 5)
(fact1 n)

    (if (> 5 10) 1 2)

    ; if statmeent -> true case -> false case 
    ; = ( = 5 5 ) -> if (5 == 5) in scheme 


(define (compare x y) 
    (cond 
        ((> x y) "> 10")
        ((< x y) "< 2")
        ((> x y) "> 1")
        (else "Nothing ")
        )
)

(define (compare x y)
    (cond 
        ((> x y) "> 10")
        ((< x y) "< 2")
        ((> x y) "> 1")
        (else "Nothing ")
    )
)


(define (f1 n1) 

    (cond 
        ((= n1 0) 1)
        (else (* n1 (f1 (- n1 1))))
    )

)

(and (> 5 3) (> 4 5)) ;#f 
(and (> 5 3) (> 4 1)) ;#f 
(or (> 5 3) (> 4 1)) ;#f 


(define (var1 x) 

    (cond 
        ((= (modulo x 5) 0) 1 )
        (else "Nope ")
    )
    
)




(display (cons 1 4))
(cdr (cons 1 4))
(list '(1 2 5 10) '(1 3))


; functions --------->

(string-append "Hello" " there") ; appends the strings 
;.scm extension 


(define (func1 name) 
(string-append "Hello " name ) ; appends the strings 
)

; if true -> true -> else ----
;'A -> characters 




(list-ref '(2 3 4) 1)