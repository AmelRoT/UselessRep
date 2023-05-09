program playingAround

    double precision :: a1
    integer :: a2
    double precision,allocatable , dimension(:) :: a3
    integer :: n 
    double precision f1 
    real(KIND=8) :: a_1,a11,a22
    n = 100
    a11 = 20
    a22 = 30
    allocate(a3(n))
    a1 = 200
    a2 = 2

    do i = 1,100,1 

        if(i <= 50) then
            a3(i) = a1*a2 
        else 
            a3(i) = i
        end if 
        print *, "A3 : " 
        print *, a3(i) 


    end do  
    write(*,*) f1(a1) 
    call subrutina(a11,a22,a_1)
    print *, a_1
    deallocate(a3)
    
end program 


function f1(x)

    double precision :: f1,x 
    f1 = x+x  

end function 


subroutine subrutina(a1,a2,a_final)
    
    real(KIND = 8),intent(in) :: a1,a2
    real(KIND = 8),intent(out) :: a_final


    a_final = (a1*a2)+20
end subroutine 
