
import sys 

# first tut on python 

# def function_name()
    # have to indent to assign the block

a = 200

def print_a() : 
    global a 
    print("Global is : ", a)

print_a()

a2 = 300
def print_a2() : 

    print("Global is : ", a2)

print_a2()


    