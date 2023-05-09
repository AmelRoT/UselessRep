(newline)

; ------------------------ Display function -------------------------

(display "whetever")
(display 10) 

; -----------------------------Define functions ----------------------------------


(define x 100)
(display x)
(define x (+ 3 5)) ; adds two numbers 
(display x)

; doing 10*2+(6-4) in function  = 22 

(define x1 (+ (* 10 2) (- 6 4))) ; 22 
(display x1)

(define (y x) (+ x 2)) 
(define (f1 x) (* x x 2))
(display (f1 2))


(define (y a b) (+ (* a b) 2 )) ; 8 
; you may define variables names immediately and the parameters that are required to be taken and utilized later on 
(display (y 2 3))

; --------------------------- If function -----------------------

; (= x y)	x is equal to y
; (> x y)	x is greater than y
; (< x y) 	x is less than y

; (and (= x y) (< y z)) 
; (or (= x y) (< y z))
; (not (= x y))
; (and (= 5 5) (< 5 6))
; (and (= 5 5) (< 5 5))

; Simple If else statement 
(define (x x1) 
    (if (= x1 1) "Yes " "No")
)

(define (fact n) 

    (if (= n 1) 1 (* n (fact (- n 1))))

)

(display (fact 5))

 ; you may use Cond with else if and at the end else to write down the conditions 

(define (x a b) 

    (cond 
        ((< a b) b)
        ((> a b) a) 
        (else "Equal")
    )
)

(display (x 10 5)) 

(define (leap year) 

    (cond 
    
        ((= (modulo year 400) 0 ) "Leap" ) 
        ((= (modulo year 100) 0 ) "Not Leap" ) 
        ((= (modulo year 4) 0 ) "Leap" ) 
        (else "Not leap")
    )


)

 ; ---------------------------------Working with Lists --------------------------------
(define (x1 a) a)
(diplay (x1 '(1 2 3))) ; it would be a list 


(display (car '(1 2 3)))
(display (car (cdr '(1 2 3))))
(display (car (cdr (cdr '(1 2 3)))))


(define (sum1 l1) 
    (cond 
        ((null? l1) 0 )
        ( (+ (car l1) (sum1 (cdr l1))))
        (else "this ")
        )
    )

    (display sum1 '(1 2 3))
    
(define (sum_list lis)
    (cond 
          ((null? lis) 0)
          (else (+ (car lis) (sum_list (cdr lis))))
    ))



(define (fact x) 

    (if (= x 1) 1 
    
        (* x (fact (- x 1)))
    
    )
)

(display (fact 10))



(define (someRandom x y )

    (cond 
    
        ((and ( > x y) (> x 5))  "x")
        ((or ( < x y) (< 2 y)) "y")
        (( = x y) "=")
        (else "This") 
    )

)

(display (someRandom 5 1))

(define (value1 x )

    (
        if (= (remainder x 5) 0) "yes"
        "NO" 
    )





)
(define (value2 x )

    (
        if (zero? (modulo x 5)) "yes"
        "NO" 
    )

)



(display (car '(1 2 3)))

(display (null?(cdr '()))) ; or car of '() is an error
; so cdr has to be taken from the list if the list is (1) - 1 element it would return () - empty 
; cdr of empty list is error 


(display (null? '())) ; #t
(display (null? '(1 2))) ; #f

; What can we do with the list -> car, cdr ?? 

(display (car'((1 2) 2))) ; (1 2), does not return an atom but a list 

(display (car (cdr '(A B C))))

; Using Quote - or ' 

(display '(1 23 23)) ; equivalent to the bottom quote version
(display (quote (1 23 23)))

; writing 'A = A in display 

(display 'A) ; -> gives A 

; --------------------------- cons, list, appends ---------------------
;cons builds the list from two arguments : 
    ; 1. an atom or a list 
    ; 2. list 

(display (cons 'A '())) ; (A)
(display (cons 'B '(1 2 3))) ; (B 1 2 3)
(display (cons '(1 2) '(1 2 3))) ; ((1 2) 1 2 3)

(display (cons '(1) '(1 2 (3)))) 



; list would be used to make two seperate lists or add elements inside the list 
(display (list 'A '())) ; (A ()) 
(display (list 'A )) ; (A) , you may use just one argument 
(display (list '(1 2) '(1 2 3))) ; ((1 2) (1 2 3))
(display (list 'A 'B 'C)) ; it would be useful to use atoms and turn them into a list
(display (list 'A '(1 2)))

(display 'A)
(display 1)
(display (cons 1 '(1 2)))

(display (cons (car '(A B)) (cdr '(A B))))
; append removes both of the intial () 

(display (append '(A B C) '(A B C)))
(display (append '(A B C) '(A (B C))))

; difference between append and cons is that append removes both of the initial () while cons only removes the () of the list 
(display (append 'A '(A B C))) ; append only concatinates lists  and that is why this returns an error.

; 3 predicate functions : 
    ; 1. eq? -> two preciates are atoms and are equal it return #t 
    ; 2. list? -> tests if the parameter is a list or not 
    ; 3. null? -> returns true if the parameter is an empty list 

(display (eq? 'A 'B)) ; #f
(display (eq? 'A 'A)) ; #t
(display (eq? '(A) '(A))) ; #t or #f - even if atoms are in the list , it is not reliable for the lists 

(display (list? '(1 2 3)))
(display (list? '()))
(display (list? '(A)))
(display (list? 'A)) ; only #f answer


(display (null? '())) ; tests whether the list is empty or not 



(define (add num1)

    (if (null? num1) 0
    
    ; else case 
        (+ (car num1) (add (cdr num1))) ; downward level does not work ? 

    )
)

(define (multi num1)

    (if (null? num1) 1
    
    ; else case 
        (* (car num1) (multi (cdr num1))) ; downward level does not work ? 
        
    )
)


(display (add '(1 2 3 4)))
(display (multi '(1 2 3)))

(define (sum_list lis)
   (if (null? lis) 0 
            (+ (car lis) (sum_list (cdr lis))) )
    )
(display (sum_list '(2 3 4 5)))


; member  and equalsimp ? 
 

(define (memberOrNot attom list )

    (if 
        (null? list) #f
         (if (eq? attom (car list) ) #t
            (memberOrNot attom (cdr list))
         )
         
    )
)

(display (memberOrNot 'A '(B A C )))


; equal lists ? 
(define (testList list1 list2 )


    (cond 
        ((and (null? list1) (null? list2)) "true")
        ((or (null? list1) (null? list2)) "false")
        ((eq? (car list1) (car list2)) (testList (cdr list1) (cdr list2)))
        (else "false")
    
    )

)

(display (testList '()'()))

(display (member '(1) '(1 2 3)))



(display (list 'A 'A 'A))


(define (g1 list1 list2)

    (cond 
        ((or (null? list1) (null? list2)) '())
        ((memberOrNot (car list1) list2) 
            (cons (car list1) (g1 (cdr list1) list2))
        )    
        (else (g1 (cdr list1) list2))
    )
    
    )

(display (g1 '(E A B D G) '(A B C D)))


(define (x lis)

    (cond 
    
        ((null? lis) 0) 
        ((not (list? (car lis)))
            (cond
                ((eq? (car lis) '()) (x (cdr lis)))
                (else (+ 1 (x (cdr lis))))))
        (else  (x (cdr lis)))
        ) 
    )

(display (x '(10 () 30)))


























































































































































































































