program object1
    implicit none 

    type person 

        double precision :: a 
        integer(kind = 4):: b 

    end type person 

    type(person) :: var1 


    var1%a = 10

    var1 = person(210,200)
    print *, var1%a 


end program 

