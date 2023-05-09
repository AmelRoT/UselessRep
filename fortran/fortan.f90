
function calculate_func(a, b) result(r)
    integer, intent (in) :: a, b    ! input intent(in) a and b cannot be changed
    integer              :: r       ! output intent(out) by default

    r = a+ b
end function

function calculate_func1(a, b) 
    integer, intent (in) :: a, b    
    integer              :: calculate_func1      

    calculate_func1 = a+ b
    return
end function


subroutine calculate_sub(a, b, r)
    integer, intent (in)  :: a, b           ! input
    integer, intent (out) :: r              ! output

    r = a+ b
end subroutine

program hello
   integer :: calculate_func, calculate_func1, r
   double precision :: whatever,a1,b1,c1
    
   a1 = 10.0
   b1 = 10.0
   c1 = 20
   Print *, "Result is calculate_func ", calculate_func(1,2)
   Print *, "Result is calculate_func1 ", calculate_func1(3,4)
   
   !call  calculate_sub(5,6,r)
   !  Print *, "Result is calculate_sub ", 
   
    Print *, "this is it" , whatever(a1,b1,c1)
end program Hello


double precision function whatever(a,b,c) 

    double precision,intent(in) :: a,b,c; 
    whatever = a*b+c

end function 