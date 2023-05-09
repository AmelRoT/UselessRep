function some_function(){
  console.log("Hello from some_function()");
}
some_function();

///////////////////////////////////////////////////////////////////////////////////////


function calculate_parameters(a, b){
    console.log(`a=${a}, b=${b}`);
    return a + b;
}
// call by position
let result = calculate_parameters(1,2);
console.log(`Result ${result}`);

// call using keywords
result = calculate_parameters(b=4,a=2);
console.log(`Result ${result}`);

///////////////////////////////////////////////////////////////////////////////////////

// function parameter values are allowed
function calculate_function_default(c, d=1){
    return c+d;
}    
result = calculate_function_default(10)
console.log(`Result ${result}`);


///////////////////////////////////////////////////////////////////////////////////////

// function parameter values are allowed
function calculate_functio_arguments(){
    return arguments[0]+arguments[1];
}    
result = calculate_functio_arguments(20,21)
console.log(`Result ${result}`);


///////////////////////////////////////////////////////////////////////////////////////

//function definitions can be empty
function calculate_empty(){
    
}

///////////////////////////////////////////////////////////////////////////////////////

// can have functions without name

const var_function = function(a, b) {
  return 30+31;
}
result = var_function(20+21);
console.log(`Result ${result}`);
///////////////////////////////////////////////////////////////////////////////////////

// can have method functions
let x = 0;               // source element
if (x === 0) {           // source element
  x = 10;                // not a source element
  function boo() {}      // not a source element
}
function foo() {         // source element
  let y = 2;             // source element
  function bar() {}      // source element
  while (y < 10) {       // source element
    function blah() {}   // not a source element
    y++;                 // not a source element
  }
}


function whatever(){
  return arguments[0]*arguments[1]+arguments[2]; 
}

console.log(whatever(10,20,3)); 