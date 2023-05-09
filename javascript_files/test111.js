
a = [[1,2,3,4,5], [3,2,5,4,10,10,3]]
var a11 = ""; 
function somefun(a){
    for(i = 0; i<=1; i++){
       for(j = 0 ; j<a[i].length;j++){
        a11 =a11+a[i][j]+" "; }
        console.log(a11)
        console.log()
        a11 = ""
    }    
}

somefun(a)
console.log(a[0].length);
console.log(a)