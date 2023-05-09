
a = [10,23,45]

for i in range(0,len(a)) : 
    print(a[i])
    

def function1(a,b): 
    return a+b

print(function1(10,20)) 


if(10>20) : 
    print("TRUE")
elif(30>10): 
    print("TRUE ")
else : 
    print("FALSE ")

b = [0 for x in range(3)]

print(b)
a = [[0 for x in range(1,4)], [0 for x in range(1,4)]]
print(a)


for i in range(0,2) : 
    for j in range(0,3) : 
        a[i][j] = j 
        print(a[i][j])
print(a)
print(a[0][2])
print(range(0,2))

for j1 in range(0,2) : 
    print(j1)