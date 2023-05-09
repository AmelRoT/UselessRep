program file1;

var
    numbers : real; 
    array1 : array[1..5,1..5] of integer ;
    i : integer; 
    j : integer; 
begin   

    for i := 1 to 5 do 
    begin 
        for j:= 1 to 5 do 
    begin 
        array1[i,j] := j;   
        write(array1[i,j]); 
    end ;
    writeln(); 
end
end.