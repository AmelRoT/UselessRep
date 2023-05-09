import sys 
import re
global result 

testingDigit = re.compile(r'[-]?[0-9]+\.?[0-9]*$') 

def product1(a) :
    result = 1; 
    for i in range(0,len(a)) : 
        if(testingDigit.match(str(a[i])) != None) : #testing if the input is a digit or not 
            a[i] = float(a[i]) # parsing it to float value if the string is a digit 
            result = result*a[i]
        else :
            print("Nothing")
    return result 

a11 =  [1,2,3,4,"123","123a", 2,3,"3"]
print(product1(a11))





