//-----------------------Calculator program----------------------//


//------------------------Addition-------------------------------//
function add(num1,num2){   
    result = num1+num2; 
    return result; 
}
//------------------------Subtraction----------------------------//
function subtract(num1,num2){   
    result = num1-num2; 
    return result; 
}
//------------------------Multiplication-------------------------//
function multiply(num1,num2){   
    result = num1*num2; 
    return result; 
}
//------------------------Division--------------------------------//
function divide(num1,num2){
    if(num2 == 0){ // Division by Zero is NOT ALLOWED
        console.log("Division by Zero is forbidden.");  
        return NaN; 
    }   
    result = num1/num2; 
    return result; 
}

//------------------------Remainder ------------------------//

function remainder(num1,num2) {
    num1 = Math.floor(num1); // non integer number will be round up to floor value
    num2 = Math.floor(num2);

    result = divide(num1,num2); 
    return Math.round((result-Math.floor(result))*num2);
}
//-----------------------Exponentiation ---------------------//

function exponentiate(num1,n) {
    result = 1
    if(n == 0) {  //first case x^0 = 1
        return result; 
    }

    else if (Math.abs(n-Math.floor(n))==0) {  // x^(integer)
        for (i = 1; i<= Math.abs(n) ;i++) {
          result = result*num1 
        }
        if(n>0) {
            return result;
        }
        else {
            return 1/result;
        }
    }        
    else { // x^(positive or negative decimal value)
        return exp(n*ln(num1));
    }
}
function exp(x) { 

    // Using Taylor Series
    //        inf
    //       _____
    //       \     
    // e^x =  \    x^n/n! = 1+x+x^2/2!+x^3/3! +...
    //        /    
    //       /____  
    //       n = 0

     x1 = 1; // for storing of x value 
     n = 1; // for storing of factorial value
     e1 = 1; 
    for ( i = 1; i <=100 ; i++) 
    {
        n  *= i;  // using compound assignment  n = n*i
        x1 *=  x;  // updates x and n based on the previous values 
        e1 += x1 / n; 
    }
    return e1;
}
function ln(x){
    
    // Using Taylor Series
    //             inf
    //           _____
    //           \     
    // ln(x)= 2*  \   (((x-1)/(x+1))^(2n-1))/(2n-1)
    //            /    
    //           /____  
    //            n = 1
    x1 = 1; // storing of x values 
    l1 = 0; // storing of ln prior to final return  

    for ( i = 1; i<=100; i++) // for our purposes tolarance of 10^-10 to 10^-15 is just fine
    {

        for (j = 1; j <=(2*i-1); j++) // used for odd values 2n+1 = 1,3,5,7,9 ...
        {
            x1 = (x - 1) / (x + 1) * x1;
        }
        l1 +=  (x1/(2 * i - 1));
        x1 = 1; // reset the value of x1 prior to next iteration
    }
    l1 = 2 * l1; // simply multiplying by two after the addition process
    return l1; 
} 

//-----------------------Square Root -------------------------//
function square_root(num1) {

    // we will use Fixed point iteration method for finding square root 
    // Mathematical Description : 
    // x = n^(1/2) 
    // 2*x^2 = n + x^2 -> using g(x) = x -> x = (n+x^2)/(2*x)
    // taking derivative g'(x) = 2x*(2x)^-1 + (n+x^2)*(-4*x) -> 1-(n+x^2)/(4*x) 
    // therefore g'(x) < 1 and the function will converge for any value of n. 
    
    result = 1.0; // first iteration xo = 1

    for( i = 1; i <= 40; i++)
    {
        result = (num1 + (result * result)) / (2 * result); 
    }

    return result; 
}
//-------------------------End of Functions---------------------------//

/*  //---------------------------HW 1--------------------------------//

// ----------------------------Addition -----------------------------//
console.log("--------------------------Addition 1---------------------"); 
console.log("5.1 + 5.23 = " + addition(5.1,5.23)); 
console.log("--------------------------Addition 2---------------------"); 
console.log("-10 + 3 = " + addition(-10,3)); 

// ----------------------------Subtraction --------------------------//
console.log("--------------------------Subtraction 1------------------"); 
console.log("-5 - 20 = " + subtraction(-5,20)); 
console.log("--------------------------Subtraction 2------------------"); 
console.log("200.5 - 150.5 = " + subtraction(200.5,150.5));

// ----------------------------Multiplication------------------------//
console.log("--------------------------Multiplication 1---------------"); 
console.log("10.10 * 30 = " + multiplication(10.10,30)); 
console.log("--------------------------Multiplication 2---------------"); 
console.log("-150 * 2.5 = " + multiplication(-150,2.5)); 

// ----------------------------Divison-------------------------------//
console.log("--------------------------Divsion 1---------------------"); 
console.log("1 / 0 = " + division(1,0)); 
console.log("--------------------------Divsion 2---------------------"); 
console.log("5/(-20) = " + division(5,-20)); 

//-----------------------End of Calculator program----------------------//

//---------------------------End of HW 1--------------------------------// */


console.log("\t ------------------ \t Calculator Operators \t -----------------")
console.log("\t | Key |\t  \t Triggers                                |")
console.log("\t |  +  |\t  \t Sum Operation                           |")
console.log("\t |  -  |\t  \t Subtraction Operation                   |")
console.log("\t |  /  |\t  \t Division Operation                      |")
console.log("\t |  *  |\t  \t Multiplication Operation                |")
console.log("\t |  %  |\t  \t Remainder Operation                     |")
console.log("\t |  ^  |\t  \t Exponentiation Operation                |")
console.log("\t |  s  |\t  \t Square root Operation                   |")
console.log("\t |  =  |\t  \t Operation that triggers other operators |")
console.log("\t ------------------ \t End of Calculator Operators \t ---------")
console.log()
console.log("Adhere to the following specification : ")
console.log(" 1. x1 (+ | - | / | * | ^ |) x2 =                    Ex. : 10 * 20 =  ")
console.log(" 2. (+ | - | / | * | ^ |) x2 =                       Ex. : (result of first) + 30 = ")
console.log(" 3. s =  or  s x2 =                                  Ex. : sqrt(result) = or sqrt(number) = ")
console.log(" 4. Operators and Operands are seperated by space    Ex. : 10 ^ 2 ")
console.log(" 5. To execute the operation press = Enter           Ex. : 10 - 2.5  = (Enter)")
console.log(" 6. Press q or Q to exit                             Ex. : q (Enter) ");


const prompt= require("prompt-sync")({sigint:true}); // this is just to take input prompt from cmd - you may delete it and test it in browser 
// you will require prompt - sync node module to run the code in vs, otherwise as mentioned previosuly, run it in browser without it 

test1 =(/[-]*[0-9]+\.?[0-9]* (\+|\*|\/|\%|\-|\^)/g) 
test2 = (/(\+|\*|\/|\%|\-|\^|s) [-]*[0-9]+\.?[0-9]*/g)

// Format 1 : number(pos or neg) followed by operator
// Format 2 : operator followed by a number(pos or neg)
// Format 3 : operator followed ny operator - implemented with else case


while(true){ 

    inline_input = prompt() // inline input 
    inline_splitting = inline_input.split(/[ ]+/) // splitting the input with space
    if(inline_splitting[0].toLowerCase() === "q") { // it will take into account both q and Q inputs 
        break
    }    
    if(((inline_input.match(test1) != null))) { // Format 1 - case 1 
        num1 = parseFloat(inline_splitting[0])
        operator1 = inline_splitting[1]
        num2 = parseFloat(inline_splitting[2])

        if(inline_splitting[3] === "=") { // if = is pressed by the user 

            switch(operator1){ 
                case "+" : 
                { 
                    result = add(num1, num2);
                    break; 
                }
                case "-" : 
                { 
                    result = subtract(num1, num2);
                    break; 
                }
                case "*" : 
                { 
                    result = multiply(num1, num2);
                    break; 
                }
                case "/" : 
                { 
                    result = divide(num1, num2);
                    break;   
                }  
                case "^" : 
                { 
                    result = exponentiate(num1, num2);
                    break;   
                }        
                case "%" : 
                { 
                    result = remainder(num1, num2);
                    break;   
                }     
                default : {
                    console.log("Wrong Input - Follow the Instructions ")
                    break; 
                }
                     
            }
            console.log(result) // console.loging result after the result execution
        }
    }
    else if(((inline_input.match(test2) != null))) { // Format 2 - case 2 
        operator1 = inline_splitting[0]
        num2 = parseFloat(inline_splitting[1])

        if(inline_splitting[2] === "=") { // if = is pressed by the user 

            switch(operator1){ 
                case "+" : 
                { 
                    result = add(result, num2);
                    break; 
                }
                case "-" : 
                { 
                    result = subtract(result, num2);
                    break; 
                }
                case "*" : 
                { 
                    result = multiply(result, num2);
                    break; 
                }
                case "/" : 
                { 
                    result = divide(result, num2);
                    break;   
                }  
                case "^" : 
                { 
                    result = exponentiate(result, num2);
                    break;   
                }        
                case "%" : 
                { 
                    result = remainder(result, num2);
                    break;   
                }        
                case "s" : 
                { 
                    result = square_root(num2);
                    break;   
                }  
                default : {
                    console.log("Wrong Input - Follow the Instructions ")
                    break; 
                }   
            }
            console.log(result) // console.loging result after the result execution
        }
    }
    else { // Format 3 - case 3 

        operator1 = inline_splitting[0]
        if(inline_splitting[1] === "="){
            if(operator1 === "s") {
                result = square_root(result); 
                console.log(result);
            }
            else {
                console.log("Wrong Input - Follow the Instructions ")
            }
        }
    }

}
console.log("-----------------------End of Calculator -------------------")
  
//---------------------End of HW 2 Testing ----------------------//
