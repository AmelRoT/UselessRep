module m1 

    integer :: a2222,a22 
    double precision :: a123
    real(KIND =4 ) :: r1

    contains 

        double precision function returnDummyMulti(x,y,z)

            integer(KIND =8) :: x,y,z
            returnDummyMulti = x*y*z

         end function    

         subroutine returnMulti(x,y,z,OUT)

            integer(KIND =8),intent(in) :: x,y,z
            integer(KIND =8),intent(out) :: OUT
            OUT = x*y*z
         end subroutine  

end module 

