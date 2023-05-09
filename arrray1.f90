program testArray 

    implicit none 
    double precision, dimension(100:200 ) :: array1
    integer :: i 

    do i = 1,100,5 ! ----> it means that (1 to 6 ) and incremented by 2 

        array1(i+100) = i 
        print *, i
    end do 

     

end program 
 