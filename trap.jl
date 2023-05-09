#-------------------Trapezoid Rule--------------------

#stepping the interval by

a = 0
b = 2
n = 100
    Iby = (b-a)/n
x = a:Iby:b
y = x.^2

T = 0;
for i in 1:length(x)

    if(x[i]==a || x[i] == b)
        T =[T Iby/2*(y[i])]
    end

    if(x[i]!=a && x[i]!=b)
        T =[T Iby/2*(2*y[i])]
    end

end

A = sum(T)
