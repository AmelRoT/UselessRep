program usingM1
    use m1
    implicit none 
    integer(KIND = 8) :: a1,a2,a3,v1
    a1 = 10
    a2 = 20
    a3 = 30
    call returnMulti(a1,a2,a3,v1) 
    write(*,*) v1
    write (*,*) returnDummyMulti(a1,a2,a3)

end program 