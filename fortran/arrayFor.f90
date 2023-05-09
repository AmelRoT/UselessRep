program for
    
    double precision :: a1; 
    double precision, dimension(5) :: a2; 
    integer , dimension(3,3) :: a3; 

    do i = 1,3
       do j = 1,3

        a3(i,j) = j; 
        print *, a3(i,j)
       end do 
    end do 


end program  for 