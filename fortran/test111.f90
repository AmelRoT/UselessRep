
program test111

    implicit none 
    integer :: a1 ,x
    double precision :: someRandom,i,j
    double precision :: y123
    double precision :: y1
    integer :: fun1
    double precision,dimension(2,2) :: array1 
    integer :: i11,i22; 

    

    a1 = 100 
    i = 30
    j = 5
    x = 5
    read(*,*) y1 ! taking input in fortran lang 
    Print *, y1

    if(a1>= i .and. a1>= j) then 
        Print *, "it is greater"

    else 
        Print *, "it is what it is "
    end if 

    write(*,*) someRandom(i)
    print *, someRandom(i)
    call someSub(j,j,y123)
    print *, y123
    write(*,*) fun1(x)
    call printing(array1)
    i22 = 0; 
    i11 = 1; 
    do while(i11 == 1)

        if(i22 == 10) then
            
            i11 = 2; 
            
         end if 
         Print *, i22 
         i22  = i22+1; 
    end do 


end program 

double precision function someRandom(x)
    double precision :: x
    someRandom = ( x*x)

end function 

subroutine someSub(x1,x2,y11)
    double precision, intent(in) :: x1,x2
    double precision, intent(out) :: y11
    y11 = x1*x2
end 

recursive integer function fun1(x) & 
result(res1)
    integer,intent(in):: x
    if(x>1) then 
        res1 = x*fun1(x-1)
    else 
        res1 = 1
    end if 


end function 

 subroutine printing(x) 
    double precision, dimension(2,2):: x

    do i = 1,2,1
        do j = 1,2,1
            x(i,j) = i
            Write(*,"(3f8.3)",advance="no") x(i,j)
        end do 
        Print *," "
    end do 
    
end subroutine
