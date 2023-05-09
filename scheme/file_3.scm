

; 100 - 5*(y^2+10)

(define (x y) (- 100 (* 5 (+ (* y y) 10))) )
(display (x))
(define (x) (- 100 (* 5 (+ 1 10))) )



(define (Celsius_to_Faren C) (+ (* C (/ 9 5)) 32 ))
(display (Celsius_to_Faren 100))



(define (fact x) 
    (if (= x 1 ) 1  ; in scheme the operation comes first - be aware 

        (* x (fact (- x 1)))
    )

)
(display (fact 4))


(define (fact1 n) 

    (cond  ; using cond to mean the same as the if -> else statement 

        ((= n 1) 1)
        (else (* n (fact1 (- n 1))))
    
    )
)

(display (fact1 5))


(define (testNumberZero x ) 

    (cond 
        ((zero? (modulo x 10)) " yes")
        (else "No")
    
    )

)


(display (testNumberZero 25 ) ) 



(define (testNumberZero x ) 

    (cond 
       ((not(= x 5)) #t)  ; use not (=  testing ) for != in scheme 
        ;((>= x 5) " yes") ; you may use >= or  <= in the comparison 
        (else #f)
    
    )

)

(display (testNumberZero 25 ) ) 



; moving on to car and cdrs 


(display (car (cdr '( 1 2 3 ))))



(display (null? '()))

; getting the sum of the list 

(define (sumOfList list1)


    (cond 
        ((null? list1) 0)
        (else (+ (car list1) (sumOfList (cdr list1))))  

    )

)

(display (sumOfList '(1 2 10 10)))


; cons adds the () at the first atom or a list and removes it on the second one -> 1.st list or an atom , 2nd list  

(display (cons '(1 2) '(2 3 4))) ; ((1 2) 2 3 4)
(display (cons 'A '(2 3 4))) ; (A 2 3 4) -> it does not remove () at the first just for the second parameter 

;append - 2 lists 

(display (append '(1 2) '(2 3 4)))  ; (1 2 2 3 4) - removes both of them because it expects two lists - first item can not be an ATOM 
(display (append 'A '(2 3 4))) ; error.  
(display (append '(1  23 2) '(2  5 6 (3) 4)))  

; null - testing if the list is empty 
(display (null? '())) ; #t
(display (null? '(1 2 3))) ; #f

; 3 predicate functions : 
    ; 1. eq? -> two preciates are atoms and are equal it return #t 
    ; 2. list? -> tests if the parameter is a list or not 
    ; 3. null? -> returns true if the parameter is an empty list 

(display (eq? 'A 'A )) ; #t
(display (eq? 'A 'B )) ; #f
(display (eq? '(1 2) '(2 1) )) ; !!! can not be used for the lists !!! 



; finding a member of the list 


(define (findMember x listt)

    (cond 
        ((null? listt) #f)
        ;((= x (car listt)) #t) ; = can be used in numbers 
        ((eq? x (car listt)) #t) 
        (else (findMember x (cdr listt)))
    )
)
(display (findMember 'A '(A B C)))

; fiding if the lists are equal or not? 


(define (listEqual list1 list2)

    (cond 
        ((and (null? list1) (null? list2)) #t)
        ((or (null? list1) (null? list2)) #f)
        ((eq? (car list1) (car list2 )) (listEqual (cdr list1) (cdr list2)))
        (else #f)    
    )
)

(display (listEqual '(A B C) '(B A C))) 


(define (newList list1 list2)

    (cond 
    
       ; ((and (null? list1) (null? list2)) '())
        ((or (null? list1) (null? list2))  '())
        ((findMember (car list1) list2) 
            (cons (car list1) (newList (cdr list1) list2))
        )
        (else  (newList (cdr list1) list2))
    
    )

)
(display (newList '( A D E A B) '(A B C D)))






(define (x y) (* y 2))
(display (x 5))


(define (fact x ) 

    (cond 
        ((= x 1) 1)
        (else (* x (fact (- x 1))))
    
    )
)

(display (fact 5))


(define (addFirstTwo list )

    (+ (car list) (car (cdr list))) 
)

(display (addFirstTwo  '(1 25 3 4)))


(define (addingElements list)

    (cond 
        ((null? list ) 0) 
        (else (+ (car list) (addingElements (cdr list))))
    
    )

)
(display (addingElements '(1 2 3 10)))


(define (isThere a list)

    (cond 
        ((null? list) #f) 
        ((eq? a (car list)) 
            #t        
        )    
        (else (isThere a (cdr list))) 
    )
)

(display (isThere  'a1 '()))

; returns number of zeros in the list 

(define (numberOfZerso list) 

    (cond 
        ((null? list ) 0 )
        ((eq? (car list) 0 ) (+ 1 (numberOfZerso (cdr list))))
        (else  (numberOfZerso (cdr list)))
    
    )
)

(display (numberOfZerso '(1 0 0 0 0 5 0 10 20))) 



(define (largest list)


    (cond 
        ((null? list ) 0)
        (else( max (car list) (largest (cdr list))))

    )
)

(define (minimum list)


    (cond 
        ((null? list ) +inf.0)
        (else( min (car list) (minimum (cdr list))))

    )
)


(display (minimum '(1 2 0.3 4 5)))


(> (car '(20 30)) '())