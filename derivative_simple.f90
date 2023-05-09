    module derivative 

        implicit none 
        ! step size h -> 
        double precision,parameter  ::  h = 0.000001


        contains 
            double  precision  function f(x)
                
                double precision :: x 
                f = x**2

            end function 

            double precision function der(x)
                double precision :: x

                der = (f(x+h)-f(x))/h

            end function 

    end module      

