import sys 
import re


print(re.findall(r'amel|AMEL', 'asdlkasdamelasdlasAMELAMEL'));  # this is with the OR function 
print(r'this is this '); 



text = 'What is going ONNNNN' 


t1 ='5554-454687-889877' 



p1  = re.compile(r'[56]554[.-]\d'); 
m1 = p1.finditer(t1); 

for i in m1: 
    print(i)

string1 = "231amelrambab@live.com 123nedim123@outlook.com 123banjo@gmail.com 123nedim1234@outlook.com wahsdhasdWhatWhatWOO" 
string2 = "amso-bomso"
p2 = re.compile(r'[a-z]+(\d{3,4}|\D)@(live|gmail|outlook)\.com' ); 
p3 = re.compile(r'(What)')
p4 = re.compile(r'(?<!\-)[a-z]+(?=bomso)') # after it 
p5 = re.compile(r'[a-z]+(?=\-)') #before it 

s1 = "Amar-...-Mujezinovic"
s1 = "asdasdasdasd123123-335-332151asdasdas3"
s22 = "AMLELELE213123123ALSDLASDL"
p6 = re.compile(r'(?<=\-)[a-zA-z]+')
p6 = re.compile(r'[\d]+\-[\d]+\-[\d]+')
p7 = re.compile(r'[a-z]+', re.I) 
print(p6.search(s1))

print(p7.search(s22))
m2 = p2.finditer(string1)
m3 = p6.finditer(s1)

#for i in m2: 
 #   print(i)


s111 = "123123132amelEmail@gmail.com aa@gmail.com 213123asdasd231eldin@outlook.com21323"




f111 = re.compile(r'[a-zA-Z]+@(gmail|outlook)(.com)')
f3 = re.compile(r'[\d]+')
m4 = f111.finditer(s111)
#print(f111.finditer(s111))
m5 = f3.finditer(s111)
for i in m5: 
    print(i)

s111 = "adinrambabovic@gmail.com"

p66 = re.sub(r'@[a-z]+(\.com)',r'',s111)
print(p66+"this")

string1 = "10123123123.1231123213123 -sadsdas"
string2 = "* 12.3"
string3 = "s = "
test1 = re.compile(r'[0-9]+\.?[0-9]* (\+|\*|\/|\%|\-|\^)')
test2 = re.compile(r'(\+|\*|\/|\%|\-|\^|s) [0-9]+\.?[0-9]*')
test3 = re.compile(r's =')

m5 = test1.match(string1)
m6 = test2.match(string2)
m7 = test3.match(string3)
print(m5 == None)
print(m6 == None)
print(m7 == None)

print("here ")

test1 = re.compile(r'[-]*[0-9]+\.?[0-9]*\s*(\+|\*|\/|\%|\-|\^)') # used Regex for testing three possible formats 
test2 = re.compile(r'\s*[-]*[0-9]+\.?[0-9]*\s*(\+|\*|\/|\%|\-|\^)\s*[-]*[0-9]+\.?[0-9]*\s*=?')

test2 = (r'\s*[-]?[0-9]+\.?[0-9]*\s*(\+|\*|\/|\%|\-|\^)\s*[-]*[0-9]+\.?[0-9]*\s*=?')
str1 = "whatever"
#t2 = str1+input(str1)
print("Newline")

#var1 = input()
#print(var1)
#t_store = re.split('(\+|\*|\/|\%|\-|\^)',var1)
#print(t_store)


#t23 = float(t_store[2])
#print(t23+10)
#regex101 - decent website for testing 

test_number =re.compile(r'[0-9]+\.?[0-9]*')
test_number_with_spaces =re.compile(r'\s*[0-9]+\.?[0-9]*\s*$')
test_space = re.compile(r'\s+')
test_operator = re.compile(r'(\+|\*|\/|\%|\-|\^)$')
test_operator2 = re.compile(r'(\+|\*|\/|\%|\-|\^|s)$')
test_case_1 = re.compile(r'\s*[-|+]?\s*[0-9]+\.?[0-9]*\s*(\+|\*|\/|\%|\-|\^)\s*[-|+]?\s*[0-9]+\.?[0-9]*\s*=?\s*$')
test_case_2 = re.compile(r'\s*(\+|\*|\/|\%|\-|\^|s)\s*[-|+]?\s*[0-9]+\.?[0-9]*\s*=?\s*')
test_case_3 = re.compile(r'\s*(s)\s*=?\s*$')
#m_value = len(t_store)


def removeSpacesInInput(input_string) : #also tests if the input is viable

    input_string_cpy = re.split('(\+|\*|\/|\%|\-|\^|s|=)',input_string)

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
            print("here ")
            for i in range(0,len(input_string_cpy),1) : 

                if(i == 0 and input_string_cpy[i] == "-" and test_number.match(input_string_cpy[i+1])!=None) : 
                    # [ "-", "123"] -> [ "-123"]
                    input_string_cpy[i+1] = input_string_cpy[i]+input_string_cpy[i+1]
                    input_string_cpy.remove("-")

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
                if((i+2) < len(input_string_cpy) and test_operator.match(input_string_cpy[i])!=None and input_string_cpy[i+1] == "+" and test_number.match(input_string_cpy[i+2])!=None) : 
                    # ["operator" "+", "123"] -> ["operator" "+123"]
                    input_string_cpy[i+2] = input_string_cpy[i+1]+input_string_cpy[i+2]
                    input_string_cpy.remove("+") 

        return input_string_cpy    
    else : 
        return None

#input_string = input()
#print(re.split('(\+|\*|\/|\%|\-|\^)',input_string))
#input_string = removeSpacesInInput(input_string)
#print("Final  : ")
#print(input_string)




# ^ negates the search [^b] -> not matching the b 
string1 = "whatever"
#s2 = input(string1)

string2 = "dasdasdads123.123+123123.123"
t_store = test_case_1.finditer(string2)

for i in t_store : 
    print(i.group())


test_number =re.compile(r'[0-9]+\.?[0-9]*')
test_number_with_spaces =re.compile(r'\s*[0-9]+\.?[0-9]*\s*')
test_space = re.compile(r'\s+')
test_operator = re.compile(r'(\+|\*|\/|\%|\-|\^)$')
test_operator2 = re.compile(r'(\+|\*|\/|\%|\-|\^|s)$')
test_case_1 = re.compile(r'\s*[-|+]?\s*[0-9]+\.?[0-9]*\s*(\+|\*|\/|\%|\-|\^)\s*[-|+]?\s*[0-9]+\.?[0-9]*\s*=?\s*')
test_case_2 = re.compile(r'\s*(\+|\*|\/|\%|\-|\^|s)\s*[-|+]?\s*[0-9]+\.?[0-9]*\s*=?\s*')
test_case_3 = re.compile(r'[-|+]?\s*[0-9]+\.?[0-9]*\s*=?\s*(\+|\*|\/|\%|\-|\^)')
test_case_4 = re.compile (r's=')

string2 = "whatever1123.1231231+123123.123123="
string22 = "asdasd10"

def function123(string_input2) : 

    # test cases -> 

    # 1. First Case input followed or perceded by random input  -> Ex : asdasdasd-56+56asdasdasd -> -56+56 returned 
    # 2. Second Case input followed or perceded by random input -> Ex : asdasd^+2asdasd->  ^+2
    # 3. Random input followed by number and operator  -> Ex : asdasd-10+asdsda -> -10+
    # 4. Random input follwed by s= returns square root in console -> asdasds=asdasd -> returns s= 

    # Given can not be changed in the input execution only if possible one may add or enter the correct input 

    t1 = test_case_1.finditer(string_input2)
    t2 = test_case_2.finditer(string_input2)
    t3 = test_case_3.finditer(string_input2)
    t4 = test_case_4.finditer(string_input2)

    t_store = None 


    for i in t1 : 
        t_store = i.group()

    if(t_store != None ) :
        return t_store

    for i in t2 : 
        t_store = i.group()

    if(t_store != None ) :
        return t_store
    
    for i in t3 : 
        t_store = i.group()

    if(t_store != None ) :
        return t_store
    
    for i in t4 : 
        t_store = i.group()

    if(t_store != None ) :
        return t_store
    
    while(True) : # user will remain in loop until the input entered is satisfactory
        string_input = input()
        if(function123(string_input)!=None) : 
            break
        
    return string_input

#print(new_input_value)
j = []




j1 = [1]
m = 1 
for i in range(m,10,1) : # m is keeping track of 

    j = j+[i]
    m = m+1


print(j)


storage1 = []


def addingElementsToList(storage,element) : 
    storage = storage+[element]
    return storage 

def takingElementFromList(storage,element) : 
    element = int(element)
    if(element <= len(storage)) : 
        return storage[element-1]
    else : 
        print("Result does not exist at location")


def printingElements(storage) : 
    for i in range(0,len(storage),1) : 
        print(f" | R{i+1} | = {storage[i]} ")


i11 = 0
#while(True) : 
##    value = input()
 #   storage1 = addingElementsToList(storage1,value)
 #   print(storage1)
 #   print(takingElementFromList(storage1,value))
 #   printingElements(storage1)





def removeSpacesInInput(input_string) : #also tests if the input is viable


    test_number =re.compile(r'[0-9]+\.?[0-9]*')
    test_number_with_spaces =re.compile(r'\s*[0-9]+\.?[0-9]*\s*')
    test_space = re.compile(r'\s+')
    test_operator = re.compile(r'(\+|\*|\/|\%|\-|\^)$')
    test_operator2 = re.compile(r'(\+|\*|\/|\%|\-|\^|s)$')
    test_case_1 = re.compile(r'\s*[-|+]?\s*[0-9]+\.?[0-9]*\s*(\+|\*|\/|\%|\-|\^)\s*[-|+]?\s*[0-9]+\.?[0-9]*\s*=?\s*$')
    test_case_2 = re.compile(r'\s*(\+|\*|\/|\%|\-|\^|s)\s*[-|+]?\s*[0-9]+\.?[0-9]*\s*=?\s*$')
    test_case_3 = re.compile(r'\s*(s)\s*=?\s*$')
    input_string_cpy = re.split('(\+|\*|\/|\%|\-|\^|s|=)',input_string) 
        
    test_case_r1 = re.compile(r'\s*R[0-9]+\s*(\+|\*|\/|\%|\-|\^)\s*[-|+]?\s*[0-9]+\.?[0-9]*\s*=?\s*$')
    test_case_r2 = re.compile(r'\s*[-|+]?\s*[0-9]+\.?[0-9]*\s*(\+|\*|\/|\%|\-|\^)\s*R[0-9]+\s*=?\s*$')
    test_case_r3 = re.compile(r'\s*(\+|\*|\/|\%|\-|\^|s)\s*R[0-9]+\s*=?\s*$')
    test_case_r4 = re.compile(r'\s*R[0-9]+\s*=?\s*(\+|\*|\/|\%|\-|\^)\s*R[0-9]+\s*=?\s*$')


    input_string_cpy = re.split('(\+|\*|\/|\%|\-|\^|s|=)',input_string)

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
            print("here ")
            for i in range(0,len(input_string_cpy),1) : 

                if(i == 0 and input_string_cpy[i] == "-" and test_number.match(input_string_cpy[i+1])!=None) : 
                    # [ "-", "123"] -> [ "-123"]
                    input_string_cpy[i+1] = input_string_cpy[i]+input_string_cpy[i+1]
                    input_string_cpy.remove("-")

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
                if((i+2) < len(input_string_cpy) and test_operator.match(input_string_cpy[i])!=None and input_string_cpy[i+1] == "+" and test_number.match(input_string_cpy[i+2])!=None) : 
                    # ["operator" "+", "123"] -> ["operator" "+123"]
                    input_string_cpy[i+2] = input_string_cpy[i+1]+input_string_cpy[i+2]
                    input_string_cpy.remove("+") 

        return input_string_cpy    

    elif(test_case_r1.match(input_string)!=None or test_case_r2.match(input_string)!=None or test_case_r3.match(input_string)!=None or test_case_r4.match(input_string)!=None) : 

        for i in range(0,len(input_string_cpy),1) : 
              input_string_cpy[i] = input_string_cpy[i].strip()
        print(input_string_cpy)

        for i in range(0,len(input_string_cpy),1) : 
            if(i< len(input_string_cpy) and input_string_cpy[i] == "") :  # it will ignore the second part if i exceeds len
                input_string_cpy.remove("")   

        return input_string_cpy

        

    else : 
      return None

#string11 = input()
#a1 = removeSpacesInInput(string11)
#print(a1)

#r123 = re.split('R',a1[0])
#print(r123[1])

string2 = input()
test_case_r1 = re.compile(r'\s*R[0-9]+\s*(\+|\*|\/|\%|\-|\^)\s*[-|+]?\s*[0-9]+\.?[0-9]*\s*=?\s*')

t11 = test_case_r1.finditer(string2)

for i in t11 : 
    print(i.group())



#if((test1.match(inline_input) == None and test2.match(inline_input) == None and test3.match(inline_input)== None and test_number.match(inline_input)!=None) 
#            or ((test_r5.match(inline_input) != None  or test_r6.match(inline_input) != None) and 
 #          (test_r1.match(inline_input) == None and test_r2.match(inline_input) == None and test_r3.match(inline_input) == None and test_r4.match(inline_input) == None)) 
 #   ) :








