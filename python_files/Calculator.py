#------------------------Calculator ----------------------#
import sys
import math
import re

#-----------------------Addition--------------------------#
def add(num1,num2) : 
    result = num1+num2
    return result
#-----------------------Subtraction-----------------------#
def subtract(num1,num2) : 
    result = num1-num2 
    return result
#-----------------------Multiply--------------------#

def multiply(num1,num2) : 
    result = num1*num2
    return result
#-----------------------divide--------------------------#
def divide(num1, num2) : 
    if(num2 == 0) : 
        print("divide by Zero is NOT allowed !")
        return float('NaN') # casting NAN from string 
    result = num1/num2
    return result
#------------------------Remainder ------------------------#

def remainder(num1,num2) : 
    num1 = math.floor(num1) # non integer number will be round up to floor value
    num2 = math.floor(num2) 

    result = divide(num1,num2) 
    return round((result-math.floor(result))*num2) 

#-----------------------Exponentiation ---------------------#

def exponentiate(num1,n) : 
    result = 1
    if(n == 0) :  # first case x^0 = 1
        return result  
    elif(abs(n-math.floor(n))==0) :  # x^(integer)
        for i in range(1,int(abs(n)+1),1) : # to avoid calculating positive and negative seperately 
          result = result*num1 
        if(n>0) : 
            return result 
        else : 
            return 1/result # x^-n = 1/x^n - where x^n is calculated above 
    else : # x^(positive or negative decimal value)
        # y = x^n -> ln(y) = (n*ln(x))
        # -> y = e^(n*ln(x)) 
        return exp(n*ln(num1)) 
    

def exp(x) : 
            # Using Taylor Series
            #        inf
            #       _____
            #       \     
            # e^x =  \    x^n/n! = 1+x+x^2/2!+x^3/3! +...
            #        /    
            #       /____  
            #       n = 0
    x1 = 1
    n = 1
    e1 = 1
    for i in range(1,101,1) : 
        n  *= i  #  1, 2! , 3! (depends on the previous value)
        x1 *=  x # just updates x and n, it depends on the previous inputs 
        e1 += x1/n   
    return e1 

def ln(x) : 
            # Using Taylor Series
            #           inf
            #          _____
            #          \     
            # ln(x)= 2* \   (((x-1)/(x+1))^(2n-1))/(2n-1)  x > 0 
            #           /    
            #          /____  
            #            n = 1

    if(x>0) : 
        x1 = 1
        l1 = 0
        for i in range(1,101,1) : 
            for j in range(1,2*i,1) : 
                x1 = ((x-1)/(x+1))*x1
            l1 = l1+(x1/(2*i-1))
            x1 = 1 # just resets the value 
        l1 = 2*l1 
        return l1 

    
#-----------------------Square Root -------------------------#
def square_root(num1) : 
    # we will use Fixed point iteration method for finding square root 
    # Mathematical Description : 
    # x = n^(1/2) 
    # 2*x^2 = n + x^2 -> using g(x) = x -> x = (n+x^2)/(2*x)
    # taking derivative g'(x) = 2x*(2x)^-1 + (n+x^2)*(-4*x) -> 1-(n+x^2)/(4*x) 
    # therefore g'(x) < 1 and the function will converge for any value of n. 
    result = 1
    for j in range(1,41,1) : 
        result = (num1+(result*result))/(2*result)
    return result

#----------------------------------End of Functions--------------#

#-------------------------Testing Functions - HW 1 ---------------#

#print("------------------ Calculator-------------------------")

#print("------------------ add 1-------------------------")

#print("1.5 + 10 = " + str(add(1.5,10)))

#print("------------------ add 2-------------------------")

#print("-15.5 + 10.5 = " + str(add(-15.5,10.5)))

#print("------------------ subtract 1----------------------")

#print("-5.2 - 10 = " + str(subtract(-5.2,10)))

#print("------------------ subtract 2----------------------")

#print("20 - 10 = " + str(subtract(20,10)))

#print("------------------ multiply 1-------------------")

#print("30 * 6.2 = " + str(multiply(30,6.2)))

#print("------------------ multiply 2-------------------")

#print("-100 * 3.5 = " + str(multiply(-100,3.5)))

#print("------------------ divide 1 ------------------------")

#print("1 / 0 = " + str(divide(1,0)))

#print("------------------ divide 2 ------------------------")

#print("-3 / 10 = " + str(divide(-3, 10)))

#print("------------------ End of Calculator------------------")

#------------------------End of Calculator - HW 1 ------------------#

#--------------------------HW 2 Testing --------------------#


print("\t ------------------ \t Calculator Operators \t -----------------")
print("\t | Key |\t  \t Triggers                                |")
print("\t |  +  |\t  \t Sum Operation                           |")
print("\t |  -  |\t  \t subtract Operation                      |")
print("\t |  /  |\t  \t divide Operation                        |")
print("\t |  *  |\t  \t multiply Operation                      |")
print("\t |  %  |\t  \t Remainder Operation                     |")
print("\t |  ^  |\t  \t Exponentiation Operation                |")
print("\t |  s  |\t  \t Square root Operation                   |")
print("\t |  =  |\t  \t Operation that triggers other operators |")
print("\t ------------------ \t End of Calculator Operators \t ---------")
print()
print("Adhere to the following specification : ")
print(" 1. x1 (+ | - | / | * | ^ |) x2 =                    Ex. : 10 * 20 =  ")
print(" 2. (+ | - | / | * | ^ |) x2 =                       Ex. : (result of first) + 30 = ")
print(" 3. s =  or  s x2 =                                  Ex. : sqrt(result) = or sqrt(number) = ")
print(" 4. Operators and Operands are seperated by space    Ex. : 10 ^ 2 ")
print(" 5. To execute the operation press = Enter           Ex. : 10 - 2.5  = (Enter)")
print(" 6. Press q or Q to exit                             Ex. : q (Enter) ")


test1 = re.compile(r'[-]*[0-9]+\.?[0-9]* (\+|\*|\/|\%|\-|\^)') # used Regex for testing three possible formats 
test2 = re.compile(r'(\+|\*|\/|\%|\-|\^|s) [-]*[0-9]+\.?[0-9]*')

# Format 1 : number(pos or neg) followed by operator
# Format 2 : operator followed by a number(pos or neg)
# Format 3 : operator followed by operator (this is implemented with else case)

while(True): 

    inline_input = input() # inline input 
    inline_splitting = inline_input.split() # using split to have each input converted to appropriate type
    if(inline_splitting[0].lower() == "q") : # it will take into account both q and Q inputs
        break
    if(((test1.match(inline_input) != None))) : # Format 1 - first case 
        num1 = float(inline_splitting[0]) # first number 
        operator1 = inline_splitting[1] # operator (+ | - | / | * etc )
        num2 = float(inline_splitting[2]) # second number 

        if(inline_splitting[3] == "=") : # if = is pressed by the user 

            if(operator1 == "+") : 
                result = add(num1, num2)
            elif(operator1 == "-") : 
                result = subtract(num1, num2)
            elif(operator1 == "*") : 
                result = multiply(num1, num2)
            elif(operator1 == "/") : 
                result = divide(num1, num2)
            elif(operator1 == "%") : 
                result = remainder(num1, num2)
            elif(operator1 == "^") : 
                result = exponentiate(num1, num2) 
            else : 
                print("Wrong Input - Read Instructions")                  
        print(result) # printing result after the result execution

    elif (((test2.match(inline_input) != None))) : # Format 2 - second case  

        operator1 = inline_splitting[0] # second number, first number is the result (0 by default)
        num2 = float(inline_splitting[1])

        if(inline_splitting[2] == "=") : # if = is pressed by the user 

            if(operator1 == "+") : 
                result = add(result, num2)
            elif(operator1 == "-") : 
                result = subtract(result, num2)
            elif(operator1 == "*") : 
                result = multiply(result, num2)
            elif(operator1 == "/") : 
                result = divide(result, num2)
            elif(operator1 == "%") : 
                result = remainder(result, num2)
            elif(operator1 == "^") : 
                result = exponentiate(result, num2)    
            elif(operator1 == "s") : 
                result = square_root(num2)
            else : 
                print("Wrong Input - Read Instructions")                 
        print(result) # printing result after the result execution
    else : 
        operator1 = inline_splitting[0]
        if(inline_splitting[1] == "=") : # if = is pressed by the user 

            if(operator1 == "s") : 
                result = square_root(result)   
                print(result) # printing result after the result execution
            else : 
                print("Wrong Input - Read Instructions")     
print("-----------------------End of Calculator -------------------")
    
#---------------------End of HW 2 Testing ----------------------#

