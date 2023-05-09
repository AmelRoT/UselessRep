
!s--------------simple interface utilization------------!
program inter1

    implicit none 
    real :: sum3 
    real :: a1,b1

    interface sum
        real function sum1(a,b)
        implicit none 
        real, intent(in) :: a,b 
        end function 

        integer function sum2(a,b)
        implicit none 
        integer, intent(in) :: a,b
        end function 

    end interface 

    a1 = 10.5
    b1 = 20.5
    sum3 = sum(a1,b1)
    
    print *, sum3 


end program 


real function sum1(a,b)
    implicit none 
    real, intent(in) :: a,b 
    sum1 = a+b 

end function 


integer function sum2(a,b)
    implicit none 
    integer, intent(in) :: a,b
    sum2 = a+b

end function 

