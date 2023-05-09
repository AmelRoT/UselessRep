# function definition
def some_function():
#"""This is documentation string"""
  print("Hello from some_function()")

# function call
some_function()

###########################################

def calculate_parameters(a, b):
    print(f"a={a}, b={b}")
    return a + b
    
# call by position
result = calculate_parameters(1,2)
print(f"Result {result}")

# call using keywords
result = calculate_parameters(b=4,a=2)
print(f"Result {result}")


###########################################

# functions with arbitraty arguments with arguments, passed in as tuples
def calculate_args(*numbers):
    print(numbers)
    return numbers[0] + numbers[1]

result = calculate_args(10, 11)
print(f"Result {result}")


###########################################

# In Python we can pass list of key-value (keyword) arguments
def calculate_kwargs(**numbers):
    print(numbers)
    return numbers['num1'] + numbers['num2']
result = calculate_kwargs(num1=10, num2=11)
print(f"Result {result}")


###########################################

# Defalt parameter values are allowed
def calculate_default(c, d=1):
    return c+d
    
result = calculate_default(10, 11)
print(f"Result {result}")


###########################################

#method definitions cannot be empt, but can use pass keyword

def calculate_empty():
    pass



b1 = 100
a1 = 200
c1 = a1+b1
print(f"{a1} + {b1} = {c1}") # f is similar to $ in the C#


def passMore(*pass1) : 
    return pass1[0]+pass1[1]+pass1[2]


print (passMore(10,20,40,1000))