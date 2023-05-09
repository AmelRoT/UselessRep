program GOTO

    implicit none 
    integer :: x,y 
    y = 5 
    x = y+3.0 

    go to 12 

    x = x+1; 
    print *, x 
    12 x = 200   
    print *, x 



end program


