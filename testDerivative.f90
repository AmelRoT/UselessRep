program  testDerivative 

    use derivative
    implicit none 

    double precision :: x
    x = 5
    write(*,*) der(x) 

end program 