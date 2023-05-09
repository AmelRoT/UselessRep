program test11;

var
    a1 : integer;
    a2 : integer ; 
    a3 : array[1..2,1..2] of integer;
    i : integer;
    j : integer; 

function someRandom(a11,a22 : integer ) : integer; 
    begin 
        someRandom := a11*a22; 
    end;

begin   
{
    writeln('Enter your number in a range from 0 - 100 ');
    readln(a1); 
    while((a1 >100) or (a1<0)) do   
        begin 
        writeln('Incorret range - enter again'); 
           if((a1<=100) and (a1>=0)) then
            begin 
                break;
            end;
           readln(a1); 
        end; 

    if(a1 mod 2 = 0) then
        begin 
         writeln('Your number is even');
        end
     else 
        begin 
            writeln('Your number is odd');
        end    
}

{
    writeln('Enter your value in the given range '); 
    readln(a2);
    
    while((a2>100) or (a2<0)) do

        begin 
            writeln('Enter it again : '); 
            readln(a2); 
        end; 
    
    if(a2 mod 2 = 0) then 
    begin 
    
        writeln('Even '); 

    end
    else 
    begin 
        writeln('Odd'); 
    end;
}
{
for i := 1 to 5 do 
    begin 
        a3[i] := i+2; 
        writeln(a3[i]); 
    
    end; 
}

for i := 1 to 2 do 
    begin 
    for j:= 1 to 2 do 
    begin 
        a3[i,j] := i+2; 
        write(a3[i,j]);
        write(' ');  
        end;
        writeln(' ');
    end; 
    a1 := 15; 
    a2 := 3; 
    a2 := someRandom(a1,a2);
    writeln(a2); 
end.
//---

