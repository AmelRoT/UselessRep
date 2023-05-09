program testintSubroutine 
 implicit none 
 integer :: sum 
 integer :: add1 

 call addition1(5,25,add1) 
 sum = add1 
 print *, sum 

end program testintSubroutine


subroutine addition1(a,b,add1) !inputs and outputs combined -> different from other languages  

    integer , intent(in) :: a,b 
     integer ,intent(out) :: add1 
     add1 = a+b

end subroutine addition1

