# -------------------------------Lecture 12.12.2022 - PL ---------------------#

# Functional Programming Language -> FPL short notation
# .scm for scheme extension 
# functional programming languages -> Chapter 15 
# The focus is on the scheme 

# 1. Intro 
# 2. Mathematical Functions 
# 3. Some coding in Scheme
# 4. Haskell and ML 
# 5. Applicationns of Functional languages 

# Imperative lang. -> Von Neumann architecture (variables, assignment statement and iterations)
# Efficiency is the primary concern of the imperative langauges 
# Functional PL are better than Imperative languages due to reliabiliy, readable etc 

#Functional programming lang : LISP(most commonly utilized lang.) , ML , COMMON LISP , Haskell, Scheme(just a dialect of the LISP) 

# mapping 
# Domain set -----------------> Range set  

    #a           --->               # I              
    #b                              # II           
    #C                              # III   
    #d                              # IV 

# lambda is the nameless function lambda(x) (x*x*x)
#  cube(x) = x*x*x  

# h(x) = f(g(x))
# f  = x+2 
# g = 3+x 
# h(x) = (3+x) +2  ||| g = f o g 
# alfa applied to all -> each element of the list
 
# h(x) = x*x 
#alfa (h (2,3,4))- > (4, 9, 16)
# iteration is not possible in functional langauges -> controlled by variables -> repetition is done by recurssion in FPL 
# Data object types -> atoms and lists 
# list -> (A,B,C,D ) and (A,B, (C,D), E ), (C,D ) represent the sublist in the list 
# atom -> numeric literal or the character  
# two pointers , first to atom the second one to the second element in the list 
# -> [o o] -> [ o o ] -> [ o o ] --> [ o \ ] (A, B, C ,D )
#     A         B           C          D 

# Ex : (1 (2 (3 4 )))
# [ o o ] -> [ o /]
#  1           |
#              V           
#             [o /] -> [ o /] 
               #2      [ o o ]

# ------------------------ Covering the Scheme ---------------# 
# static scoping only 
# the functions are first class entities 
# first class entity : 
# 1. occur in the expression 
# 2. asssign to a variable 
# 3. can be used as a parameter 
# 4. can be retured by a function call 

#Ex : int of Java is the first class entity, for some lang. the functions are not 1st class entity, however, in scheme they are 
#doubleNumbeR(int x){
#   x = x*2; 
#   return x; 
# }

# Scheme is the interpreted languages. -> line by line interpration.
# read - evaluate - write 
# f(x,y) = x+y 
# x = 2
# y = 3 
# # 2+3 -> 5 (then it is printed) 


# ----------------------------Scheme Coding ---------------------------#
#(display "Hello World")
#(newline)
#(display (+ 3 6))
#(display (+ 3 7))
#(display (+ 3 8))
#(display "Hello World")
#(newline)
#(display (- 20 10 ))
#(newline)
#(lambda(x) (*x x ) 5)
#(define x1 10)
#(display x1)
#(display "Hello World")
#(newline)
#(display (- 20 10 ))
#(newline)
#(lambda(x) (*x x ) 5)
#(define x1 10)
#(display x1)
#(newline)
#(define x2 (+ 10 20))
#(display x2)

#(display (+))
#(newline)
#(display (*))
#(newline)

#(define y (+ (* 2 (+ 3 4)) (- 10 5)))
#(display y)
#(newline)
#(define z (+(/ 16 4)(* 2.1 (- 12 7)) (/ 100 2)) )
#(display z)

# ----------------------------------Lectrue 13- > 19.12.2022-------------------# 




