console.log("What is going on"); 

var var1; 
function testFunction1(){
    var1 = 30; // it is global unless one specifies it to be local 
    return var1; 
} 

let var2 = 10;  // block assignment even if the value is changed in the function it is local and does not affect the answer
function testFunction2(){
    var2 = 30; // it is global unless one specifies it to be local 
    return var2; 
} 


console.log(testFunction1());
console.log(var1); 
var1 = "Hello There"; 
console.log(var1); 
console.log(testFunction1());
console.log(var2); 
var2 = "Hello There"; 
console.log(var2); 