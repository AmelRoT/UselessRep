program ifStatement

    double precision :: var1 
    integer :: var2,i 

    var1 = 300
    var2 = 200
    i = 10

    if(var1 > 300) then 
        print *, "Var1 is greater than 300 "
    else if (var2 >= 200) then 
        print *, "Var2 is greater than or equal to 200"
        print *, "Just to demonstrate the block structure"
    else 
        print *, "dummy i variable is equal to 10" 
    end if 



end program 