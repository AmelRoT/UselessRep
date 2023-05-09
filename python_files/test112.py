import sys

def someFunction(a): 
    if(a[1][0] != None) : 
        for i in range(0,len(a[:])) : 
            for j in range(0,(len(a[i][:]))) : 
                print(a[i][j], end = " ")
            print()
a11 = [[1,3,5],[1,4,5,6,7,5], [2 ,3 ,5, 10],[2 ,3 ,5 ,6]]
a12 = [1,2,3]
someFunction(a11)
print()
someFunction(a12)
print()

def printing(array11) : 
    for i in range(0, len(array11)) : 
        print(array1[i], end = " ")
    print()

printing(array1)