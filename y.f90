module y

    implicit none 
    contains 
    double precision function f(x)
        double precision :: x 
        f= x**2 

    end function 

    double precision function f1(x)
    double precision :: x 
    f1= x**3

    end function 

    double precision function f2(x)
    double precision :: x 
    f2= x**4 

    end function 

    double precision function f3(x)
    double precision :: x 
    f3= x**5 

    end function 





end module 