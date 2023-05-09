program pointer1
    implicit none   
    integer, pointer :: p1 
    integer,target  :: a1 ! in order to point to a specific variable a1 has to be target
    integer, pointer :: p22
    integer, target :: p123
    
    type objeakt1 

    double precision :: aa2,a12
    integer (KIND =4) :: a123
    integer, pointer :: aPoint
    end type  
    type(objeakt1) :: var1

    var1%aPoint => p123
    var1%a123 = 100
    p1 => a1 
    a1 = 100 
    print *, p1

    p22 => p123 

    p123 = 300 
    print *, p123
    write(*,*) var1%aPoint
    print *, var1%a123


end program 

