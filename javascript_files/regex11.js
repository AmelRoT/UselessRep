var inStr = "abc123xyz456_7_00AAA";
var newString = "123-334asdasdasd-12sdsadasdasd3"
// Use RegExp.test(inStr) to check if inStr contains the pattern
console.log(/[0-9]+/.test(inStr));  // true
console.log(inStr.match(/[0-9]+[a-zA-Z]+/g)); // it has to be global for the whole text

//console.log(inStr.replace(/\d+/, "**"));   // abc**xyz456_7_00
//console.log(inStr.replace(/\d+/g, "**"));  // abc**xyz**_**_**
//console.log(inStr.replace(/[a-z]+(\d{3,5})[a-z]+/, "+-+")) 
newString = "amelramdedovic@gmail.com"
newString = newString.replace(/[a-zA-z]+/g, "")
newString = newString.replace(/(amel)/, "adin");
//console.log(newString);
//console.log(newString1010);
  
// we are at our weakest point here, you are just required to write faseter and that is about it. 

console.log("here")

test1 =(/[-]*[0-9]+\.?[0-9]* (\+|\*|\/|\%|\-|\^)/g) 
test2 = (/\s*(\+|\*|\/|\%|\-|\^|s)\s*[-|+]*[0-9]+\.?[0-9]*\s*/g)
string = "-123123.123123 -"
string2 = "+ -123.123123"

console.log((string.match(test1) != null))
console.log((string2.match(test2) != null))


const prompt=require("prompt-sync")({sigint:true}); 
var a1 = prompt()
//a2 = a1.split(/[ ]+/)
//a3 = a1.split(/(\+|\*|\/|\%|\-|\^|s)/) 
//console.log(a3)

//a4 = [4,a3[1].replace(/\s*/g,"")]
/*
console.log(a4)

console.log((a1.match(test2)==null))
console.log(a4[1]) // string starts from 0

console.log(parseFloat(""))


*/
function Input_with_or_without_spaces(input_string){

    test_number =(/[0-9]+\.?[0-9]*/g)
    test_number_with_spaces =(/\s*[0-9]+\.?[0-9]*\s*/)
    test_space = (/\s+/)
    test_operator = (/(\+|\*|\/|\%|\-|\^)$/)
    test_operator2 =(/(\+|\*|\/|\%|\-|\^|s)$/)
    test_case_1 = (/^\s*[-|+]?\s*[0-9]+\.?[0-9]*\s*(\+|\*|\/|\%|\-|\^)\s*[-|+]?\s*[0-9]+\.?[0-9]*\s*=?\s*$/)
    test_case_2 = (/^\s*(\+|\*|\/|\%|\-|\^|s)\s*[-|+]?\s*[0-9]+\.?[0-9]*\s*=?\s*$/)
    test_case_3 = (/^\s*(s)\s*=?\s*$/)
    var input_string_cpy = input_string.split(/(\+|\*|\/|\%|\-|\^|s|=)/) 
    
    // Test cases for R[number] -> 
    // 1. R[number] follwed by Real number -> R11+10 
    // 2. Real number followed by R[number] -> 10 + R1
    // 3. operator followed by R[number]-> +R20 = result + R20
    // 4. R[number] followed by R[number] -> R10+R20 

    test_case_r1 = (/^\s*R[0-9]+\s*(\+|\*|\/|\%|\-|\^)\s*[-|+]?\s*[0-9]+\.?[0-9]*\s*=?\s*$/)
    test_case_r2 = (/^\s*[-|+]?\s*[0-9]+\.?[0-9]*\s*(\+|\*|\/|\%|\-|\^)\s*R[0-9]+\s*=?\s*$/)
    test_case_r3 = (/^\s*(\+|\*|\/|\%|\-|\^|s)\s*R[0-9]+\s*=?\s*$/)
    test_case_r4 = (/^\s*R[0-9]+\s*=?\s*(\+|\*|\/|\%|\-|\^)\s*R[0-9]+\s*=?\s*$/)


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


// Test cases for R[number] -> 
// 1. R[number] follwed by Real number -> R11+10 
// 2. Real number followed by R[number] -> 10 + R1
// 3. operator followed by R[number]-> +R20 = result + R20
// 4. R[number] followed by R[number] -> R10+R20 


hh1 = ["1","2",]
hh1.splice(1,1)
console.log("here")
//console.log(someFunction(a1))
console.log(hh1)

s = []
s.push(123)   
console.log(s)
s.push(100)
console.log(s)
console.log(s[0])



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
console.log("asdasdasdAAAA")
a = []
a = addingElementsToList(a,10)
a = addingElementsToList(a,20)
console.log(a)
console.log(takingElementFromList(a,2))
console.log(takingElementFromList(a,10))
console.log(printingElements(a))



//----------------------------------------------Incorrect handling function -------------------------------------------------------------------------//
function incorrectInputHandling(string_input2) {

    // end of the string is excluded from test_cases ($)
    test_case_1 = (/\s*[-|+]?\s*[0-9]+\.?[0-9]*\s*(\+|\*|\/|\%|\-|\^)\s*[-|+]?\s*[0-9]+\.?[0-9]*\s*=?\s*/)
    test_case_2 = (/\s*(\+|\*|\/|\%|\-|\^|s)\s*[-|+]?\s*[0-9]+\.?[0-9]*\s*=?\s*/)
    test_case_3 = (/[-|+]?\s*[0-9]+\.?[0-9]*\s*(\+|\*|\/|\%|\-|\^)/)
    test_case_4 = (/s=/)
    test_case_5 = (/[0-9]+/)
    test_case_6 = (/\D+/)
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
    test_case_r1 = (/\s*R[0-9]+\s*(\+|\*|\/|\%|\-|\^)\s*[-|+]?\s*[0-9]+\.?[0-9]*\s*=?\s*/g) 
    test_case_r2 = (/\s*[-|+]?\s*[0-9]+\.?[0-9]*\s*(\+|\*|\/|\%|\-|\^)\s*R[0-9]+\s*=?\s*/)
    test_case_r3 = (/\s*(\+|\*|\/|\%|\-|\^|s)\s*R[0-9]+\s*=?\s*/)
    test_case_r4 = (/\s*R[0-9]+\s*=?\s*(\+|\*|\/|\%|\-|\^)\s*R[0-9]+\s*=?\s*/)
    test_case_r5 = (/\s*R[0-9]+\s*(\+|\*|\/|\%|\-|\^)\s*/) // if aaaaR1+aaaa> start from R1+
    test_case_r6 = (/\s*R[0-9]+\s*/) // if aaaaR1aaaa> start from R1 

    p1 = (/\s*(p|P)\s*$/) //in case user presses p or M 
    m1 = (/\s*(m|M)\s*$/) // in case user presses m or M 


    t1 = string_input2.match(test_case_1)
    t2 = string_input2.match(test_case_2)
    t3 = string_input2.match(test_case_3)
    t4 = string_input2.match(test_case_4)
    t5 = string_input2.match(test_case_5)
    t6 = string_input2.match(test_case_6)
    tr1 = string_input2.match(test_case_r1)
    tr2 = string_input2.match(test_case_r2)
    tr3 = string_input2.match(test_case_r3)
    tr4 = string_input2.match(test_case_r4)
    tr5 = string_input2.match(test_case_r5)
    tr6 = string_input2.match(test_case_r6)


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

    if(t5 != null ) {
        return 0
    } 

}
// ----------------------------------------------- End of Incorrect Input  Handling -------------------------------------//
test_case_1 = (/\s*[-|+]?\s*[0-9]+\.?[0-9]*\s*(\+|\*|\/|\%|\-|\^)\s*[-|+]?\s*[0-9]+\.?[0-9]*\s*=?\s*/)

string1 = prompt()

//console.log((string1.match(test_case_1)))
//a = (string1.match(test_case_1) == null)
//console.log(a[0] == null)

//console.log(Input_with_or_without_spaces(string1))
 input_string_cpy1 = string1.split(/R/g) 

console.log(input_string_cpy1[1])

console.log("Enter")
string1 = string1+prompt(string1)
console.log(string1)
console.log("--------------------")
string10 = "100+"
test_number = (/^\s*[0-9]+\.?[0-9]*\s*(\+|\*|\/|\%|\-|\^)+\s*$/g)
test_case_3 = (/^\s*s\s*=?\s*$/)

console.log(string10.match(test_case_3) == null)
console.log("--------------------")



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