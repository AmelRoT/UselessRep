import sys
import math
import re


def someFunc(arg1, arg2, arg3, *args, **kwargs): # it is waiting for the keyword paramrs **, * for array arguments or lists 
    print(arg1) 
    print(arg2)  
    print(arg3)
    print(args)
    print(kwargs)
    return 0 


list2 = [1, 5, 7, 9, 3,5,6]
someFunc(list2,2,4,5,76,list2,10, tue=72, wed=77)




