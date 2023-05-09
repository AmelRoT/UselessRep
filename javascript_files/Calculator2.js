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
    num1 = Math.abs(num1) // negative input is converted to positive, no negative sqrt
    for( i = 1; i <= 40; i++)
    {
        result = (num1 + (result * result)) / (2 * result); 
    }

    return result; 
}

//--------------------------------------------Input with Multiple or None spaces(Involving Rn)----------------------------------------//
function Input_with_or_without_spaces(input_string){

    test_number =(/[0-9]+\.?[0-9]*/g)
    test_operator = (/(\+|\*|\/|\%|\-|\^)$/g)
    test_operator2 =(/(\+|\*|\/|\%|\-|\^|s)$/g)
    test_case_1 = (/^\s*[-|+]?\s*[0-9]+\.?[0-9]*\s*(\+|\*|\/|\%|\-|\^)\s*[-|+]?\s*[0-9]+\.?[0-9]*\s*=?\s*$/g)
    test_case_2 = (/^\s*(\+|\*|\/|\%|\-|\^|s)\s*[-|+]?\s*[0-9]+\.?[0-9]*\s*=?\s*$/g)
    test_case_3 = (/^\s*(s)\s*=?\s*$/g)

    var input_string_cpy = input_string.split(/(\+|\*|\/|\%|\-|\^|s|=)/) 

    
    if(input_string.match(test_case_1) != null || input_string.match(test_case_2) != null  || input_string.match(test_case_3) != null ) {
        
        //  --------------- Removing Spaces from the Input ---------------------//
        for(i = 0; i<input_string_cpy.length; i++){
            input_string_cpy[i] = input_string_cpy[i].replace(/\s*/g,"")
        }

        for(i = 0; i<input_string_cpy.length; i++){
            if(input_string_cpy[i] == ""){
                input_string_cpy.splice(i,1)
            }
        } // removes all of the unnecessary spaces in between [123,"" , + "", 123] = [123,+,123]

        if(input_string.match(test_case_1) != null){

            for(i = 0; i < input_string_cpy.length; i++){ 

                if(i == 0 && input_string_cpy[i] == "-" && input_string_cpy[i+1].match(test_number) != null) {
                    input_string_cpy[i+1] = input_string_cpy[i]+input_string_cpy[i+1]
                    input_string_cpy.splice(i,1)
                    }
                if(i == 0 && input_string_cpy[i] == "+" && input_string_cpy[i+1].match(test_number) != null) {
                    input_string_cpy[i+1] = input_string_cpy[i]+input_string_cpy[i+1]
                    input_string_cpy.splice(i,1)
                     }
                if((i+2)<input_string_cpy.length && input_string_cpy[i].match(test_operator) != null &&input_string_cpy[i+1] == "-" && input_string_cpy[i+2].match(test_number) != null){
                    input_string_cpy[i+2] = input_string_cpy[i+1]+input_string_cpy[i+2]
                    input_string_cpy.splice(i+1,1)
                    }
                if((i+2)<input_string_cpy.length && input_string_cpy[i].match(test_operator) != null &&input_string_cpy[i+1] == "+" && input_string_cpy[i+2].match(test_number) != null){
                    input_string_cpy[i+2] = input_string_cpy[i+1]+input_string_cpy[i+2]
                    input_string_cpy.splice(i+1,1)
                    }
            }
         }

         else if (input_string.match(test_case_2) != null){

            for(i = 0; i < input_string_cpy.length; i++){ 

                if(i == 1 && input_string_cpy[i] == "-" && input_string_cpy[i+1].match(test_number) != null) {
                    input_string_cpy[i+1] = input_string_cpy[i]+input_string_cpy[i+1]
                    input_string_cpy.splice(i,1)
                    }
                if(i == 1 && input_string_cpy[i] == "+" && input_string_cpy[i+1].match(test_number) != null) {
                    input_string_cpy[i+1] = input_string_cpy[i]+input_string_cpy[i+1]
                    input_string_cpy.splice(i,1)
                    }
            }

         }
        return  input_string_cpy
    }
else if(input_string.match(test_case_r1) != null || input_string.match(test_case_r2) != null  || input_string.match(test_case_r3) != null || input_string.match(test_case_r4))
    {
        for(i = 0; i<input_string_cpy.length; i++){
            input_string_cpy[i] = input_string_cpy[i].replace(/\s*/g,"")
        }

        for(i = 0; i<input_string_cpy.length; i++){
            if(input_string_cpy[i] == ""){
                input_string_cpy.splice(i,1)
            }
        } 
        
        if(input_string_cpy[0] == "-" && input_string.match(test_case_r2) != null) {
            input_string_cpy[1] = input_string_cpy[0]+input_string_cpy[1]
            input_string_cpy.splice(0,1)
        }
        return input_string_cpy
    }
else
    {  
        return null; 
    }
}  

//----------------------------------------------Incorrect handling function -------------------------------------------------------------------------//
function incorrectInputHandling(string_input2) {

    // end of the string is excluded from test_cases ($)
    test_1 = (/\s*[-|+]?\s*[0-9]+\.?[0-9]*\s*(\+|\*|\/|\%|\-|\^)\s*[-|+]?\s*[0-9]+\.?[0-9]*\s*=?\s*/g)
    test_2 = (/\s*(\+|\*|\/|\%|\-|\^|s)\s*[-|+]?\s*[0-9]+\.?[0-9]*\s*=?\s*/g)
    test_3 = (/[-|+]?\s*[0-9]+\.?[0-9]*\s*(\+|\*|\/|\%|\-|\^)/g)
    test_4 = (/s=/g)
    test_5 = (/\s*[0-9]+\.?[0-9]*\s*(\+|\*|\/|\%|\-|\^)?\s*/g)
    test_6 = (/[0-9]+\.?[0-9]*/g)
    test_7 = (/\D+/g)
/*
     Given test cases -> 

     1. First Case input followed or perceded by random input  -> Ex : asdasdasd-56+56asdasdasd -> -56+56 returned 
     2. Second Case input followed or perceded by random input -> Ex : asdasd^+2asdasd->  ^+2
     3. Random input followed by number and operator  -> Ex : asdasd-10+asdsda -> -10+
     4. Random input follwed by s= returns square root in console -> asdasds=asdasd -> returns s= 
     5. If number is found it will start from the number -> Ex : asdasd10asasdasd-> 10
     6. In case Nothing is found user will have to enter again from the beginning 
     
    Given can not be changed in the input execution only if possible one may add or enter the correct input 

     Included R[number] cases ->
     1. R[number] (operator) number , if it is enclosed in wrong input it will still find it. Ex : aaRn10+2aa = R10+2
     2. number (operator) R[number] , if it is enclosed in wrong input it will still find it. Ex : aa10+Rnaa = 10+Rn
     3. [operator]R[number]  ->                                                               Ex : aaa+Rn = result+Rn  
     4. R[number] (operator) R[number]                                                        Ex : aaRn10*R20aa = R10*R20
     5. R[number] (operator)  --->                                                            Ex : aaR20+aa = R20+ (starts in console from this line)                                          
     6. just R[number] in a rondom sequence will start from R[number] -->                     Ex : aaR10aAAAa = R10  
*/
    test_r1 = (/\s*R[0-9]+\s*(\+|\*|\/|\%|\-|\^)\s*[-|+]?\s*[0-9]+\.?[0-9]*\s*=?\s*/g) 
    test_r2 = (/\s*[-|+]?\s*[0-9]+\.?[0-9]*\s*(\+|\*|\/|\%|\-|\^)\s*R[0-9]+\s*=?\s*/g)
    test_r3 = (/\s*(\+|\*|\/|\%|\-|\^|s)\s*R[0-9]+\s*=?\s*/g)
    test_r4 = (/\s*R[0-9]+\s*=?\s*(\+|\*|\/|\%|\-|\^)\s*R[0-9]+\s*=?\s*/g)
    test_r5 = (/\s*R[0-9]+\s*(\+|\*|\/|\%|\-|\^)\s*/g) // if aaaaR1+aaaa> start from R1+
    test_r6 = (/\s*R[0-9]+\s*/g) // if aaaaR1aaaa> start from R1 

    p1 = (/^\s*(p|P)\s*$/g) //in case user presses p or M 
    m1 = (/^\s*(m|M)\s*$/g) // in case user presses m or M 


    t1 = string_input2.match(test_1)
    t2 = string_input2.match(test_2)
    t3 = string_input2.match(test_3)
    t4 = string_input2.match(test_4)
    t5 = string_input2.match(test_5)
    t6 = string_input2.match(test_6)
    t7 = string_input2.match(test_7)

    tr1 = string_input2.match(test_r1)
    tr2 = string_input2.match(test_r2)
    tr3 = string_input2.match(test_r3)
    tr4 = string_input2.match(test_r4)
    tr5 = string_input2.match(test_r5)
    tr6 = string_input2.match(test_r6)


        // Handiling R[number] + only number cases with some random Input-> If input is correct  and enclosed in incorrect input it will still work
        // aaaaAAaaa10+20aaaAAAaa = 30 or aaaAaaaaR1+R2aaaAA = R1+R2 (assuming R1 and R2 are taken in memory by (m|M) )
        
    if(tr4 != null ) {
        return tr4[0] 
    }
    if(tr1 != null ) {
        return tr1[0] 
    } 
    if(tr2 != null ) {
        return tr2[0] 
    } 
    if(tr3 != null ) {
        return tr3[0] 
    } 

    if(tr5 != null ) {
        return tr5[0] 
    }
    if(tr6 != null ) {
        return tr6[0] 
    } 
    if(t1 != null ) {
        return t1[0] 
    } 
    if(t2 != null ) {
        return t2[0] 
    } 
    if(t3 != null ) {
        return t3[0] 
    } 
    if(t4 != null ) {
        return t4[0] 
    } 
    if(t5 != null ) {
        return t5[0] 
    } 

    if(string_input2.match(p1)) {
        return "p"
    }
    if(string_input2.match(m1)) {
        return "m"
    }

    if(t6 != null ) {
        return t6[0]
    }
    if(t7 != null ) {
        return "0"
    }


}
// ----------------------------------------------- End of Incorrect Input  Handling -------------------------------------//

function quitFunction(string_input){
    quit_ = (/^\s*(q|Q)\s*$/g) //in case user presses p or M 

      if(string_input.match(quit_)) {
        return 1
    }
    return null; 
}

function addingElementsToList(storage,element) { // 
    storage.push(element)
    return storage 
}

function takingElementFromList(storage,element){ 
    element = parseInt(element)
    if(element <= (storage).length) {
        return storage[element-1]
    }
    else {
        console.log("Result does not exist at location.")
        return null
    }
}
function printingElements(storage) { 
    for(i =0; i<storage.length; i++){
        console.log(`| R${i+1} | = ${storage[i]} `)
    }
    if(storage.length == 0) {
        console.log(" |  | =  empty  ")
        }
        
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
console.log("\t |  -  |\t  \t subtract Operation                      |")
console.log("\t |  /  |\t  \t divide Operation                        |")
console.log("\t |  *  |\t  \t multiply Operation                      |")
console.log("\t |  %  |\t  \t Remainder Operation                     |")
console.log("\t |  ^  |\t  \t Exponentiation Operation                |")
console.log("\t |  s  |\t  \t Square root Operation                   |")
console.log("\t |  =  |\t  \t Operation that triggers other operators |")
console.log("\t ------------------ \t End of Calculator Operators \t ---------")
console.log()
console.log("-----------------------------------------------------------------------------------------------------------------------------")
console.log("\t\t\tAdhere to the following specifications : ")
console.log("-----------------------------------------------------------------------------------------------------------------------------")
console.log("\t\t\tStorage of User Variables : ")
console.log("-----------------------------------------------------------------------------------------------------------------------------")
console.log(" 1.Pressing (M|m) keys results in storing the result")
console.log(" 2.Result is stored as a list, one may retrive elements by pressing Rn    Ex : R1+10 = takes input from R1 adds it to 10")
console.log(" 3.Pressing (p|P) keys results in printing the stored variables           EX : p displays |R1| = 10")
console.log("-----------------------------------------------------------------------------------------------------------------------------")

console.log("\t\t\tInput Functionality of Calculator(IFC) ")
console.log("-----------------------------------------------------------------------------------------------------------------------------")
console.log("  1. x1 (+ | - | / | * | ^ |) x2 =                                  Ex. : 10 * 20 =  ")
console.log("  2. (+ | - | / | * | ^ |) x2 =                                     Ex. : (result of first) + 30 = ")
console.log("  3.s =  or  s x2 =                                                 Ex. : sqrt(result) = or sqrt(number) = ")
console.log("  4. Rn (+ | - | / | * | ^ |) x1 =                                  Ex. : Rn * 20 =  ")
console.log("  5. x1 (+ | - | / | * | ^ |) Rn =                                  Ex. : 20 * Rn =  ")
console.log("  6. (+ | - | / | * | ^ |) Rn =                                     Ex. : (result of first) + Rn = ")
console.log("  7. Rn (+ | - | / | * | ^ |) Rn =                                  Ex. :  Rn + Rn =  ")
console.log("  8. Multiple or no spaces are possible                             Ex. :  10   +  10  | 10+10  ")
console.log("  9. End of input is possible with = or just (enter - key)          Ex. :  10+20 = | 10+10(press enter)  ")
console.log("  10. Press q or Q to exit                                           Ex. :  q (Enter) ")
console.log("-----------------------------------------------------------------------------------------------------------------------------")

console.log("\t\t\tExceptions are handled in the following manner : ")
console.log("-----------------------------------------------------------------------------------------------------------------------------")
console.log("1.Random Input + logical -> logical is evaluated or passed to next line      Ex : aaaAAAaaa10+10aaaAAaasd -> 20")
console.log("2.Any Rn in the string has presedence over just number                       Ex : asaaAAR1aa100aa -> starts in console from R1")
console.log("3.If all of IFC are wrong -> default case is 0                               Ex : aaaaaAAaaa -> 0(enter from there)")
console.log("5.Random input followed by Rn or number and operator, starts from that point Ex : aaaBBd5+bbbAA-> 5+(enter from there)")
console.log("6.Cases (IFC) from 1 to 7 are evaluated first                                Ex : aaaaa10   + 10 aaa100aaa -> 20 ")
console.log("7.If number is found within random input only, it starts from that number    Ex : aaaaa100aaa -> starts from 100")
console.log("8.If user inputs Rn in random sequence it will start from that Rn            Ex : aaaaR1aaaa -> R1 ")
console.log("9.If Rn inputed does not exist it will print Result does not exist at location.")
console.log("10.If number is present in random sequence it starts from that number        Ex : aaaa1200aaa -> 1200")
console.log("11.In random text if s= is present the square root is taken or s[(+|-)?Num]  Ex : aaaaas100aaaaa-> 10")
console.log("-----------------------------------------------------------------------------------------------------------------------------")


const prompt= require("prompt-sync")({sigint:true}); // this is just to take input prompt from cmd - you may delete it and test it in browser 
// you will require prompt - sync node module to run the code in vs, otherwise as mentioned previosuly, run it in browser without it 


test_space = (/\s+/g)
test_case_1 = (/^\s*[-|+]?\s*[0-9]+\.?[0-9]*\s*(\+|\*|\/|\%|\-|\^)\s*[-|+]?\s*[0-9]+\.?[0-9]*\s*=?\s*$/g)
test_case_2 = (/^\s*(\+|\*|\/|\%|\-|\^|s)\s*[-|+]?\s*[0-9]+\.?[0-9]*\s*=?\s*$/g)
test_case_3 = (/^\s*s\s*=?\s*$/)

test_number1 = (/\s*[0-9]+\.?[0-9]*\s*(\+|\*|\/|\%|\-|\^)?\s*/g) // should be ? instead of +
test_p = (/^\s*(p|P)\s*$/g)
test_m = (/^\s*(m|M)\s*$/g)

test_case_r1 = (/^\s*R[0-9]+\s*(\+|\*|\/|\%|\-|\^)\s*[-|+]?\s*[0-9]+\.?[0-9]*\s*=?\s*$/g) 
test_case_r2 = (/^\s*[-|+]?\s*[0-9]+\.?[0-9]*\s*(\+|\*|\/|\%|\-|\^)\s*R[0-9]+\s*=?\s*$/g)
test_case_r3 = (/^\s*(\+|\*|\/|\%|\-|\^|s)\s*R[0-9]+\s*=?\s*$/g)
test_case_r4 = (/^\s*R[0-9]+\s*=?\s*(\+|\*|\/|\%|\-|\^)\s*R[0-9]+\s*=?\s*$/g)
test_case_r5 = (/^\s*R[0-9]+\s*(\+|\*|\/|\%|\-|\^)\s*$/g) 
test_case_r6 = (/^\s*R[0-9]+\s*$/g) 


storage = []
result = 0; // default case for result 



while(true){ 

    inline_input = prompt() // inline input 
   
    if(quitFunction(inline_input)!=null) { // it will take into account both q and Q inputs 
        break
    }    

    inline_splitting = Input_with_or_without_spaces(inline_input)

    if(inline_splitting == null){
        while(true){

            inline_splitting = incorrectInputHandling(inline_input)
            if(inline_splitting != null){
                
                if(inline_input.match(test_p) != null)
                {
                    printingElements(storage)
                    break
                }

                if(inline_input.match(test_m) != null)
                {
                    storage = addingElementsToList(storage,result)
                    break
                }
                inline_input = inline_splitting
            }
            else{
                inline_input = prompt()
            }

            if((inline_input.match(test_case_r5) != null || inline_input.match(test_case_r6) != null || inline_input.match(test_number1) != null) && 
             (inline_input.match(test_case_r1) == null &&  inline_input.match(test_case_r2) == null &&  inline_input.match(test_case_r3) == null&& inline_input.match(test_case_r4) ==null
             && (inline_input.match(test_case_1) ==null && inline_input.match(test_case_2) ==null && inline_input.match(test_case_3) ==null)
             )){
                inline_input = inline_input + prompt(inline_input)
            }
            else{
                
                inline_splitting = Input_with_or_without_spaces(inline_input)
                break 
            }

        }
    
    }
            // ----------- Case 1 --------- number (operator ) number -----------//
    if(inline_input.match(test_case_1) != null) { 

        num1 = parseFloat(inline_splitting[0]) // ["x1" "(opeartor)" "x2"] -> num1 = x1 
        operator1 = inline_splitting[1]  // operator = operator
        num2 = parseFloat(inline_splitting[2]) // num2 = x2

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
                     
            }
            console.log(result) // console.loging result after the result execution
    }
        // ----------- Case 2---------  (operator ) number -----------//

    else if(inline_input.match(test_case_2) != null) { 
        operator1 = inline_splitting[0]
        num2 = parseFloat(inline_splitting[1])

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
            }
            console.log(result) // console.loging result after the result execution
    }
        // ----------- Case 3 ---------  (operator ) = | (s= square root) -----------//

    else if(inline_input.match(test_case_3) != null) { // Format 3 - case 3 

        operator1 = inline_splitting[0]
        result = square_root(result);
        console.log(result);

    }
            // ----------- Case 1 (User Inputs Rn)--------- Rn (operator ) number -----------//

    else if(inline_input.match(test_case_r1) != null) { 
       
        R_split = inline_splitting[0].split(/R/g)
        R_split = R_split[1]
        
        if(takingElementFromList(storage,R_split)!=null) {

            num1 = parseFloat(takingElementFromList(storage,R_split))
            operator1 = inline_splitting[1]
            num2 = parseFloat(inline_splitting[2])

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
                                  
            }
            console.log(result) // console.loging result after the result execution
        }
    }
    // ----------- Case 3 (User Inputs Rn)---------  (operator ) Rn -----------//

    else if(inline_input.match(test_case_r3) != null) { 
       
        R_split = inline_splitting[1].split(/R/g)
        R_split = R_split[1]

        if(takingElementFromList(storage,R_split)!=null) {

            num2 = parseFloat(takingElementFromList(storage,R_split))
            operator1 = inline_splitting[0]

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
            }
            console.log(result) // console.loging result after the result execution
        }
    }
    // ----------- Case 2 (User Inputs Rn)--------- number (operator ) Rn -----------//


    else if(inline_input.match(test_case_r2) != null) {  
       
        R_split = inline_splitting[2].split(/R/g)
        R_split = R_split[1]

        if(takingElementFromList(storage,R_split)!=null) {
            num1 = parseFloat(inline_splitting[0])
            num2 = parseFloat(takingElementFromList(storage,R_split))
            operator1 = inline_splitting[1]

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
                     
            }
            console.log(result) // console.loging result after the result execution
        }
    }
    // ----------- Case 4 (User Inputs Rn)---------  Rn (operator ) Rn -----------//

    else if(inline_input.match(test_case_r4) != null) { 
        R_split = inline_splitting[0].split(/R/g)
        R_split = R_split[1]

        R_split2 = inline_splitting[2].split(/R/g)
        R_split2 = R_split2[1]


        if(takingElementFromList(storage,R_split)!=null && takingElementFromList(storage,R_split2)!=null) {
            num1 = parseFloat(takingElementFromList(storage,R_split))
            num2 = parseFloat(takingElementFromList(storage,R_split2))
            operator1 = inline_splitting[1]

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
                     
            }
            console.log(result) // console.loging result after the result execution
        }
    }
}

console.log("-----------------------End of Calculator -------------------")
  
//---------------------End of HW 2 Testing ----------------------//
