program exFunction;
var
   ret : integer;

(*function definition *)
function calculate_func(a, b: integer): integer;
var
   (* local variable declaration *)
   result: integer;

begin
   result := a+b;
   calculate_func := a+b;
end; { end of function }  

procedure calculate_proc(a, b: integer; var r: integer); 
(* Calculates sum of a and b *)

begin
  r := a + b;
end; { end of procedure calculate_proc }  

function whatever(a,b : double ) : double;

begin 
   whatever := a*b; 

end; 


begin
 
   writeln( 'calculate_func result is : ', calculate_func(1, 2) );
   
    (* calling a procedure*)
   calculate_proc(3, 4, ret);
   writeln( 'calculate_func result is : ', ret );
   writeln( 'whatever result is : ', whatever(3.5, 100.11) );

end.



