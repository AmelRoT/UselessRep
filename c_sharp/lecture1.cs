
using System; 

class someClass{

static void Main(string[] args) {

        ClassTwo obj1 = new ClassTwo(); 
        obj1.x1 = 200; 
        Console.WriteLine(obj1.x1); 
        ClassTwo.x = 300; 
        Console.WriteLine(ClassTwo.x); 
        obj1.function1(120); 
        obj1.function2(ref obj1.x1); 

      } 
}
public class ClassTwo
{

    // public static int x = 200; 
    public int x1; 
    public static int x = 200; 

    public void function1(int x){
        Console.WriteLine(x);
         x = 200; 
         Console.WriteLine(x);

    }

    public void function2(ref int x){
      
         Console.WriteLine(x);
        x1 = 300; 
        Console.WriteLine(x);
      
    }
    
  

}


/*
public class Class1{

    public static int var1; 
    public int var2; 
/*
    public void Test1(int x){

    }
   
    public  void Test12(ref int x){

    }
    public  void Test31(out int x){

    }
    */


// static x  to the calss 
// instance to the object 
//  in console.writeln to specify variables {}




