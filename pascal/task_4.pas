//-------------------------------------------------Task 4 --------------------------------------//
program task4;

var
    a1 : integer; 
begin   

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
end.
//-------------------------------------------------End of Task 4 --------------------------------------//