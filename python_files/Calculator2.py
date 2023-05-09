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
    num1 = abs(num1) # only considers positive numbers -> negative is converted to positive
    for j in range(1,41,1) : 
        result = (num1+(result*result))/(2*result)
    return result
#--------------------------Space Removing Function -----------------------# 


def Input_with_or_without_spaces(input_string) : 

    test_number =re.compile(r'[0-9]+\.?[0-9]*')
    test_number_with_spaces =re.compile(r'\s*[0-9]+\.?[0-9]*\s*')
    test_space = re.compile(r'\s+')
    test_operator = re.compile(r'(\+|\*|\/|\%|\-|\^)$')
    test_operator2 = re.compile(r'(\+|\*|\/|\%|\-|\^|s)$')
    test_case_1 = re.compile(r'\s*[-|+]?\s*[0-9]+\.?[0-9]*\s*(\+|\*|\/|\%|\-|\^)\s*[-|+]?\s*[0-9]+\.?[0-9]*\s*=?\s*$')
    test_case_2 = re.compile(r'\s*(\+|\*|\/|\%|\-|\^|s)\s*[-|+]?\s*[0-9]+\.?[0-9]*\s*=?\s*$')
    test_case_3 = re.compile(r'\s*(s)\s*=?\s*$')
    input_string_cpy = re.split('(\+|\*|\/|\%|\-|\^|s|=)',input_string) 
    
    # Test cases for R[number] -> 
    # 1. R[number] follwed by Real number -> R11+10 
    # 2. Real number followed by R[number] -> 10 + R1
    # 3. operator followed by R[number]-> +R20 = result + R20
    # 4. R[number] followed by R[number] -> R10+R20 

    test_case_r1 = re.compile(r'\s*R[0-9]+\s*(\+|\*|\/|\%|\-|\^)\s*[-|+]?\s*[0-9]+\.?[0-9]*\s*=?\s*$')
    test_case_r2 = re.compile(r'\s*[-|+]?\s*[0-9]+\.?[0-9]*\s*(\+|\*|\/|\%|\-|\^)\s*R[0-9]+\s*=?\s*$')
    test_case_r3 = re.compile(r'\s*(\+|\*|\/|\%|\-|\^|s)\s*R[0-9]+\s*=?\s*$')
    test_case_r4 = re.compile(r'\s*R[0-9]+\s*=?\s*(\+|\*|\/|\%|\-|\^)\s*R[0-9]+\s*=?\s*$')


    if(test_case_1.match(input_string)!=None or test_case_2.match(input_string)!=None or test_case_3.match(input_string)!=None) : 
        for i in range(0,len(input_string_cpy),1) : 

            if(i< len(input_string_cpy) and input_string_cpy[i] == "") :  # it will ignore the second part if i exceeds len
                input_string_cpy.remove("")                               # which only happens if elements are removed 

            if(i< len(input_string_cpy) and test_number_with_spaces.match(input_string_cpy[i])!=None) : 
                input_string_cpy[i] = float(input_string_cpy[i])  # ["   123"] -> convert
                input_string_cpy[i] = str(input_string_cpy[i])    # ["123.0"] 


        for i in range(0,len(input_string_cpy),1) : 
                if(i<len(input_string_cpy) and test_space.match(input_string_cpy[i])!=None) : # [ "   ", "123"->  ["123"]]
                    input_string_cpy.remove(input_string_cpy[i])

        if(test_case_1.match(input_string)!=None) : 

            for i in range(0,len(input_string_cpy),1) : 

                if(i == 0 and input_string_cpy[i] == "-" and test_number.match(input_string_cpy[i+1])!=None) : 
                    # [ "-", "123"] -> [ "-123"]
                    input_string_cpy[i+1] = input_string_cpy[i]+input_string_cpy[i+1]
                    input_string_cpy.remove("-")

                if(i == 0 and input_string_cpy[i] == "+" and test_number.match(input_string_cpy[i+1])!=None) : 
                    # [ "+", "123"] -> [ "+123"]
                    input_string_cpy[i+1] = input_string_cpy[i]+input_string_cpy[i+1]
                    input_string_cpy.remove("+")

                if((i+2) < len(input_string_cpy) and test_operator.match(input_string_cpy[i])!=None and input_string_cpy[i+1] == "-" and test_number.match(input_string_cpy[i+2])!=None) : 
                    # ["operator" "-", "123"] -> ["operator" "-123"]
                    input_string_cpy[i+2] = input_string_cpy[i+1]+input_string_cpy[i+2]
                    input_string_cpy.remove("-")

                if((i+2) < len(input_string_cpy) and test_operator.match(input_string_cpy[i])!=None and input_string_cpy[i+1] == "+" and test_number.match(input_string_cpy[i+2])!=None) : 
                    # ["operator" "+", "123"] -> ["operator" "+123"]
                    input_string_cpy[i+2] = input_string_cpy[i+1]+input_string_cpy[i+2]
                    input_string_cpy.remove("+")

        elif (test_case_2.match(input_string)!=None) : 
            for i in range(0,len(input_string_cpy),1) : 
                if((i+2) < len(input_string_cpy) and test_operator2.match(input_string_cpy[i])!=None and input_string_cpy[i+1] == "-" and test_number.match(input_string_cpy[i+2])!=None) : 
                    # ["operator" "-", "123"] -> ["operator" "-123"] -> for the second case (result operator input)
                    input_string_cpy[i+2] = input_string_cpy[i+1]+input_string_cpy[i+2]
                    input_string_cpy.remove("-") 
                if((i+2) < len(input_string_cpy) and test_operator2.match(input_string_cpy[i])!=None and input_string_cpy[i+1] == "+" and test_number.match(input_string_cpy[i+2])!=None) : 
                    # ["operator" "+", "123"] -> ["operator" "+123"]
                    input_string_cpy[i+2] = input_string_cpy[i+1]+input_string_cpy[i+2]
                    input_string_cpy.remove("+") 

        return input_string_cpy    

    elif(test_case_r1.match(input_string)!=None or test_case_r2.match(input_string)!=None or test_case_r3.match(input_string)!=None or test_case_r4.match(input_string)!=None) : 

        for i in range(0,len(input_string_cpy),1) : 
            input_string_cpy[i] = input_string_cpy[i].strip()

        for i in range(0,len(input_string_cpy),1) : 
            if(i< len(input_string_cpy) and input_string_cpy[i] == "") :  # it will ignore the second part if i exceeds len
                input_string_cpy.remove("")   

        if(test_case_r2.match(input_string)!= None and input_string_cpy[0] == "-")  : # negative number (opeartor) R[number] 
            input_string_cpy[1] = input_string_cpy[0]+input_string_cpy[1]; 
            input_string_cpy.remove("-")
        return input_string_cpy    

    else : 
        return None    
        
#----------------------------------------------Incorrect handling function -------------------------------------------------------------------------#
def incorrectInputHandling(string_input2) :

    # end of the string is excluded from test_cases ($)
    test_case_1 = re.compile(r'\s*[-|+]?\s*[0-9]+\.?[0-9]*\s*(\+|\*|\/|\%|\-|\^)\s*[-|+]?\s*[0-9]+\.?[0-9]*\s*=?\s*')
    test_case_2 = re.compile(r'\s*(\+|\*|\/|\%|\-|\^|s)\s*[-|+]?\s*[0-9]+\.?[0-9]*\s*=?\s*')
    test_case_3 = re.compile(r'[-|+]?\s*[0-9]+\.?[0-9]*\s*(\+|\*|\/|\%|\-|\^)')
    test_case_4 = re.compile (r's=')
    test_case_5 = re.compile(r'[0-9]+')
    test_case_6 = re.compile(r'\D+')

    # Given test cases -> 

    # 1. First Case input followed or perceded by random input  -> Ex : asdasdasd-56+56asdasdasd -> -56+56 returned 
    # 2. Second Case input followed or perceded by random input -> Ex : asdasd^+2asdasd->  ^+2
    # 3. Random input followed by number and operator  -> Ex : asdasd-10+asdsda -> -10+
    # 4. Random input follwed by s= returns square root in console -> asdasds=asdasd -> returns s= 
    # 5. If number is found it will start from the number -> Ex : asdasd10asasdasd-> 10
    # 6. In case Nothing is found user will have to enter again from the beginning 
     
    # Given can not be changed in the input execution only if possible one may add or enter the correct input 

    # Included R[number] cases ->
    # 1. R[number] (operator) number , if it is enclosed in wrong input it will still find it. Ex : aaRn10+2aa = R10+2
    # 2. number (operator) R[number] , if it is enclosed in wrong input it will still find it. Ex : aa10+Rnaa = 10+Rn
    # 3. [operator]R[number]  ->                                                               Ex : aaa+Rn = result+Rn  
    # 4. R[number] (operator) R[number]                                                        Ex : aaRn10*R20aa = R10*R20
    # 5. R[number] (operator)  --->                                                            Ex : aaR20+aa = R20+ (starts in console from this line)                                          
    # 6. just R[number] in a rondom sequence will start from R[number] -->                     Ex : aaR10aAAAa = R10  

    test_case_r1 = re.compile(r'\s*R[0-9]+\s*(\+|\*|\/|\%|\-|\^)\s*[-|+]?\s*[0-9]+\.?[0-9]*\s*=?\s*') 
    test_case_r2 = re.compile(r'\s*[-|+]?\s*[0-9]+\.?[0-9]*\s*(\+|\*|\/|\%|\-|\^)\s*R[0-9]+\s*=?\s*')
    test_case_r3 = re.compile(r'\s*(\+|\*|\/|\%|\-|\^|s)\s*R[0-9]+\s*=?\s*')
    test_case_r4 = re.compile(r'\s*R[0-9]+\s*=?\s*(\+|\*|\/|\%|\-|\^)\s*R[0-9]+\s*=?\s*')
    test_case_r5 = re.compile(r'\s*R[0-9]+\s*(\+|\*|\/|\%|\-|\^)\s*') # if aaaaR1+aaaa> start from R1+
    test_case_r6 = re.compile(r'\s*R[0-9]+\s*') # if aaaaR1aaaa> start from R1 

    p1 = re.compile(r'\s*(p|P)\s*$') #in case user presses p or M 
    m1 = re.compile(r'\s*(m|M)\s*$') # in case user presses m or M 


    t1 = test_case_1.finditer(string_input2)
    t2 = test_case_2.finditer(string_input2)
    t3 = test_case_3.finditer(string_input2)
    t4 = test_case_4.finditer(string_input2)
    t5 = test_case_5.finditer(string_input2)
    t6 = test_case_6.finditer(string_input2)
    tr1 = test_case_r1.finditer(string_input2)
    tr2 = test_case_r2.finditer(string_input2)
    tr3 = test_case_r3.finditer(string_input2)
    tr4 = test_case_r4.finditer(string_input2)
    tr5 = test_case_r5.finditer(string_input2)
    tr6 = test_case_r6.finditer(string_input2)

    t_store = None 

        # Handiling R[number] + only number cases with some random Input-> If input is correct  and enclosed in incorrect input it will still work
        # aaaaAAaaa10+20aaaAAAaa = 30 or aaaAaaaaR1+R2aaaAA = R1+R2 (assuming R1 and R2 are taken in memory by (m|M) )

    for i in tr4:  # Case 4 for R[number]
        t_store = i.group()
    
    if(t_store != None ) :
        return t_store 

    for i in tr1:  # Case 1 for R[number]
        t_store = i.group()


    if(t_store != None ) :
        return t_store  

    for i in tr2:   # Case 2 for R[number]
        t_store = i.group()

    if(t_store != None ) :
        return t_store 
    
    for i in tr3:  # Case 3 for R[number]
        t_store = i.group()

    if(t_store != None ) :
        return t_store 

    for i in tr5:  # Case 5
        t_store = i.group()
    
    if(t_store != None ) : 
        return t_store 

    for i in tr6:  # Case 6
        t_store = i.group()

    for i in t1 : 
        t_store = i.group()

    if(t_store != None ) : # if asdasd10+10asdasd-> 20 is returned
        return t_store

    for i in t2 :  # if asdasdasd -10+--> -10+ is added to console 
        t_store = i.group()
    
    if(t_store != None ) : # if asdasd10+10asdasd-> 20 is returned
        return t_store

    for i in t3 : 
        t_store = i.group() 
    
    if(t_store != None ) : # if asdasd10+10asdasd-> 20 is returned
        return t_store

    for i in t4 : 
        t_store = i.group()

    if(t_store != None ) :
        return t_store

    for i in t5 :  
        t_store = i.group()

    if(t_store != None ) :
        return t_store  

#    if(t_store != None ) :
#       return t_store 

    if(p1.match(string_input2)) : 
        return "p"
    if(m1.match(string_input2)) : 
        return "m"

    for i in t6 : 
        t_store = i.group()

    if(t_store != None ) :
        return "0"
# ----------------------------------------------- End of Incorrect Input  Handling -------------------------------------#

#------------------------Quit Function -------------------#
def quit_program(q_input) :  # Added in HW3 to be handled in a function 
    test_q = re.compile(r'\s*(q|Q)\s*$') #in case user presses q or Q 
    if(test_q.match(q_input)) : 
       return 1
#------------------  Adding Elements from list------------------------------# 
def addingElementsToList(storage,element) :  #adding elements
    storage = storage+[element]
    return storage 
#------------------  Taking Elements from list------------------------------# 

def takingElementFromList(storage,element) : # taking element from the list 
    element = int(element)
    if(element <= len(storage)) : 
        return storage[element-1]
    else : 
        print("Result does not exist at location.")
        return None
#------------------  Printing Elements------------------------------# 
def printingElements(storage) :  
    for i in range(0,len(storage),1) : 
        print(f" | R{i+1} | = {storage[i]} ")
    if(len(storage) == 0) : 
        print(f" |  | =  empty  ")
#------------------End of Printing Elements------------------------------# 

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

#--------------------------HW 2->3 Testing --------------------#

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
print("-----------------------------------------------------------------------------------------------------------------------------")
print("\t\t\tAdhere to the following specifications : ")
print("-----------------------------------------------------------------------------------------------------------------------------")
print("\t\t\tStorage of User Variables : ")
print("-----------------------------------------------------------------------------------------------------------------------------")
print(" 1.Pressing (M|m) keys results in storing the result")
print(" 2.Result is stored as a list, one may retrive elements by pressing Rn    Ex : R1+10 = takes input from R1 adds it to 10")
print(" 3.Pressing (p|P) keys results in printing the stored variables           EX : p displays |R1| = 10")
print("-----------------------------------------------------------------------------------------------------------------------------")

print("\t\t\tInput Functionality of Calculator(IFC) ")
print("-----------------------------------------------------------------------------------------------------------------------------")
print("  1. x1 (+ | - | / | * | ^ |) x2 =                                  Ex. : 10 * 20 =  ")
print("  2. (+ | - | / | * | ^ |) x2 =                                     Ex. : (result of first) + 30 = ")
print("  3.s =  or  s x2 =                                                 Ex. : sqrt(result) = or sqrt(number) = ")
print("  4. Rn (+ | - | / | * | ^ |) x1 =                                  Ex. : Rn * 20 =  ")
print("  5. x1 (+ | - | / | * | ^ |) Rn =                                  Ex. : 20 * Rn =  ")
print("  6. (+ | - | / | * | ^ |) Rn =                                     Ex. : (result of first) + Rn = ")
print("  7. Rn (+ | - | / | * | ^ |) Rn =                                  Ex. :  Rn + Rn =  ")
print("  8. Multiple or no spaces are possible                             Ex. :  10   +  10  | 10+10  ")
print("  9. End of input is possible with = or just (enter - key)          Ex. :  10+20 = | 10+10(press enter)  ")
print("  10. Press q or Q to exit                                          Ex. :  q (Enter) ")
print("-----------------------------------------------------------------------------------------------------------------------------")

print("\t\t\tExceptions are handled in the following manner : ")
print("-----------------------------------------------------------------------------------------------------------------------------")
print("  1.Random Input + logical -> logical is evaluated or passed to next line      Ex : aaaAAAaaa10+10aaaAAaasd -> 20")
print("  2.Any Rn in the string has presedence over just number                       Ex : asaaAAR1aa100aa -> starts in console from R1")
print("  3.If all of IFC are wrong -> default case is 0                               Ex : aaaaaAAaaa -> 0(enter from there)")
print("  4.Random input followed by Rn or number and operator, starts from that point Ex : aaaBBd5+bbbAA-> 5+(enter from there)")
print("  5.Cases (IFC) from 1 to 7 are evaluated first                                Ex : aaaaa10   + 10 aaa100aaa -> 20 ")
print("  6.If number is found within random input only, it starts from that number    Ex : aaaaa100aaa -> starts from 100")
print("  7.If user inputs Rn in random sequence it will start from that Rn            Ex : aaaaR1aaaa -> R1 ")
print("  8.If Rn inputed does not exist it will print Result does not exist at location.")
print("  9.If number is present in random sequence it starts from that number         Ex : aaaa1200aaa -> 1200")
print("  10.In random text if s= is present the square root is taken or s[number]     Ex : aaaaas100aaaaa-> 10")
print("-----------------------------------------------------------------------------------------------------------------------------")

test1 = re.compile(r'\s*[-|+]?\s*[0-9]+\.?[0-9]*\s*(\+|\*|\/|\%|\-|\^)\s*[-|+]?\s*[0-9]+\.?[0-9]*\s*=?\s*$') # used Regex for testing three possible formats 
test2 = re.compile(r'\s*(\+|\*|\/|\%|\-|\^|s)\s*[-|+]?\s*[0-9]+\.?[0-9]*\s*=?\s*$')
test3 = re.compile(r'\s*(s)\s*=?\s*$')
test_number = re.compile(r'\s*[0-9]+\.?[0-9]*\s*(\+|\*|\/|\%|\-|\^)?\s*')
test_p = re.compile(r'\s*(p|P)\s*$')
test_m = re.compile(r'\s*(m|M)\s*$')

test_r1 = re.compile(r'\s*R[0-9]+\s*(\+|\*|\/|\%|\-|\^)\s*[-|+]?\s*[0-9]+\.?[0-9]*\s*=?\s*$')
test_r2 = re.compile(r'\s*[-|+]?\s*[0-9]+\.?[0-9]*\s*(\+|\*|\/|\%|\-|\^)\s*R[0-9]+\s*=?\s*$')
test_r3 = re.compile(r'\s*(\+|\*|\/|\%|\-|\^|s)\s*R[0-9]+\s*=?\s*$')
test_r4 = re.compile(r'\s*R[0-9]+\s*=?\s*(\+|\*|\/|\%|\-|\^)\s*R[0-9]+\s*=?\s*$')
test_r5 = re.compile(r'\s*R[0-9]+\s*(\+|\*|\/|\%|\-|\^)\s*') 
test_r6 = re.compile(r'\s*R[0-9]+\s*') 


# Format 1 : number(pos or neg) followed by operator -HW2 -> changed to smarter script with no spaces
# Format 2 : operator followed by a number(pos or neg) -HW2
# Format 3 : operator followed by operator (this is implemented with else case) - HW2

result = 0 # default value for result 
storage = [] # straoge is by default empty 

while(True): 

    inline_input = input() # inline input 

    if(quit_program(inline_input) == 1) : # it will take into account both q and Q inputs - > 1- True , 0 - False
        break
    inline_splitting = Input_with_or_without_spaces(inline_input) # using split to have each input converted to appropriate type

    if(inline_splitting == None) : # asdasd10+asdasd -> 10+(user input) or asdasdaADSADASD -> start from 0 [default case]
        while(True) : 
            inline_splitting = incorrectInputHandling(inline_input)
            if(inline_splitting != None ) : 
                if(inline_splitting.lower() == "p") : 
                    printingElements(storage)
                    break 
                if(inline_splitting.lower() == "m") : 
                    storage = addingElementsToList(storage,result)
                    break

            if(inline_splitting != None ) :     
                inline_input = inline_splitting
            else : 
                inline_input = input()

            if(((test_r5.match(inline_input) != None  or test_r6.match(inline_input) != None or test_number.match(inline_input)!=None) 
                 and (test_r1.match(inline_input) == None and test_r2.match(inline_input) == None and test_r3.match(inline_input) == None and test_r4.match(inline_input) == None
                 and test1.match(inline_input) == None and test2.match(inline_input) == None and test3.match(inline_input)== None)) 
            ) : 
                inline_input = inline_input+input(inline_input)
            else : 
                inline_splitting = Input_with_or_without_spaces(inline_input)
                break 

    # ------------------------------------Case 1 ->number (operator ) number ----------------------------------#
    if(((test1.match(inline_input) != None))) : # Format 1 - first case
        num1 = float(inline_splitting[0]) # first number 
        operator1 = inline_splitting[1] # operator (+ | - | / | * etc )
        num2 = float(inline_splitting[2]) # second number 

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
 

        print(result) # printing result after the result execution
    # ------------------------------------Case 2 -> (operator ) number ----------------------------------#

    elif (((test2.match(inline_input) != None))) : # Format 2 - second case  

        operator1 = inline_splitting[0] # second number, first number is the result (0 by default)
        num2 = float(inline_splitting[1])

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


        print(result) # printing result after the result execution               
    # ------------------------------------Case 3 -> (operator ) = or enter (s=) ----------------------------------#

    elif(((test3.match(inline_input) != None))): 
        operator1 = inline_splitting[0]
        result = square_root(result)   
        print(result) # printing result after the result execution
    
    # 4 Cases for R[number]  -> 
    # Test cases for R[number] -> 
    # 1. R[number] follwed by Real number -> R11+10 
    # 2. Real number followed by R[number] -> 10 + R1
    # 3. operator followed by R[number]-> +R20 = result + R20
    # 4. R[number] followed by R[number] -> R10+R20 

    # ------------------------------------Case 1 User -> Rn (operator) number ----------------------------------#

    elif(((test_r1.match(inline_input) != None))) : # R[number] follwed by Real number
        
        R_split_number = re.split('R',inline_splitting[0])
        R_split_number = R_split_number[1] #after splitting ["" , "number"] -> take number

        if(takingElementFromList(storage,R_split_number) != None) : 

            num1 = float(takingElementFromList(storage,R_split_number)) # first number 
            operator1 = inline_splitting[1] # operator (+ | - | / | * etc )
            num2 = float(inline_splitting[2]) # second number 

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

            print(result) # printing result after the result execution

    # ------------------------------------Case 2 User -> number (operator) Rn ----------------------------------#

    elif (((test_r2.match(inline_input) != None))) : #  Real number followed by R[number] 

        R_split_number = re.split('R',inline_splitting[2])
        R_split_number = R_split_number[1] #after splitting ["" , "number"] -> take number

        if(takingElementFromList(storage,R_split_number) != None) : 

            num2 = float(takingElementFromList(storage,R_split_number)) # first number 
            operator1 = inline_splitting[1] # operator (+ | - | / | * etc )
            num1 = float(inline_splitting[0]) # second number 

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

            print(result) # printing result after the result execution      

    # ------------------------------------Case 3 User ->  (operator) Rn ----------------------------------#

    elif (((test_r3.match(inline_input) != None))) : #  operator followed by R[number] 

        R_split_number = re.split('R',inline_splitting[1])
        R_split_number = R_split_number[1] #after splitting ["" , "number"] -> take number

        if(takingElementFromList(storage,R_split_number) != None) : 

            operator1 = inline_splitting[0] # second number, first number is the result (0 by default)
            num2 = float(takingElementFromList(storage,R_split_number))

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

            print(result) # printing result after the result execution  
    # ------------------------------------Case 4 User -> Rn (operator) Rn ----------------------------------#

    elif(((test_r4.match(inline_input) != None))) : # R[number] follwed by R[number]
        
        R_split_number = re.split('R',inline_splitting[0])
        R_split_number = R_split_number[1] #after splitting ["" , "number"] -> take number

        R_split_number2 = re.split('R',inline_splitting[2])
        R_split_number2 = R_split_number2[1] #after splitting ["" , "number"] -> take number

        if(takingElementFromList(storage,R_split_number) != None and takingElementFromList(storage,R_split_number2) != None) : 

            num1 = float(takingElementFromList(storage,R_split_number)) # first number 
            operator1 = inline_splitting[1] # operator (+ | - | / | * etc )
            num2 = float(takingElementFromList(storage,R_split_number2)) # second number 

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

            print(result) # printing result after the result execution        

print("-----------------------End of Calculator -------------------")
    
#---------------------End of HW 2->3 Testing ----------------------#

