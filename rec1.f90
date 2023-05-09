program rec1 

    implicit none 
    integer :: recurrsiveBehavior
    write(*,*) recurrsiveBehavior(10)


end program 



recursive integer function recurrsiveBehavior(n) &
 result(res1)
    integer,intent(in) :: n

    if(n == 1) then  
        res1 = 1
    else 
        res1 = n*recurrsiveBehavior(n-1)
    end if 
    return 

end function recurrsiveBehavior



