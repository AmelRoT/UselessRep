program testing 
    implicit none
    !         ___ a 
    !        /
    !       /
    !      |
    !      |  f(x) dx 
    !      | 
    !     /
    ! ___/ b     

    double precision :: delta_x
    double precision :: y 
    real :: a,b 
    double precision,allocatable, dimension(:) :: x 
    integer ::  i,n  
    double precision :: integralSum = 0    

    a = 0 
    b = 3 
    n = 100 
    allocate(x(n+1))

    delta_x = (b-a)/n
    do i = 1,(n+1)
        if(i == 1) then 
            x(i) = a
        
        else if(i==(n+1)) then 
            x(i) = b
        else 
            x(i) = x(i-1)+delta_x
        end if 
        
    end do 

    
    do i = 1,(n+1)
        if(i==1 .OR. i==(n+1)) then 
            integralSum = integralSum+delta_x/2*(y(x(i)))
        else 
          integralSum = integralSum+delta_x*(y(x(i)))
        end if 
    end do 

    print *, integralSum ! Calculates the a singel integral of a predefined function 
    deallocate(x)

end program



double precision function y(x) 
    double precision :: x
    y = (x*x)

end function 


