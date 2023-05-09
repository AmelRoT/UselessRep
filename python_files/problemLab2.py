import sys 


# 3 * 3 *3 *3 -> 3^4 
def powerFunction(b,p) :    
    if(p != 0) : 
        return b*powerFunction(b,p-1)
    else : 
        return 1


b1 = input('Enter base number :  ')
p = input('Enter power number(positive integer):  ')

print(powerFunction(float(b1), int(p)))