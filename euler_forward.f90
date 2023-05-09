program euler 

    implicit none 

    double precision :: h1 
    double precision :: a1,b1,yi,yf 
    integer :: n1,i
    double precision, allocatable ,dimension(:) :: s1,xi
    double precision :: f


    allocate(s1(n1))
    allocate(xi(n1))

    ! defining the step size of the diff function 
    a1 = 1 
    b1 = 1.5
    n1= 100 

    call step_size(a1,b1,n1,h1)
    print*, h1 



    do i = 1,(n1)
        if(i == 1) then 
           xi(i) = a1
     
        else 
            xi(i) = xi(i-1)+h1
         end if 
         !print *, xi(i)
    end do 

    !---------------------------------Initial conditions --------------------!

    yi = 1;

    !---------------------------------storing array variable -----------------!
    s1(1) = yi 

    do i = 1, (n1)

        yf = yi + h1*f(xi(i), yi)
        yi = yf
        s1(i+1) = yf
        print *, s1(i+1)
    end do 

    deallocate(s1)
    deallocate(xi)

end program


subroutine step_size(a,b,n,h)

    double precision,intent(in) :: a,b
    double precision,intent(out) :: h
    integer,intent(in) :: n 
    
    h = (b-a)/n 

end subroutine   

double precision function f(x,y)

    double precision :: x, y 

    f = 2*x 

end function 



