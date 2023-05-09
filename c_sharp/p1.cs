public class ClassOne
{

    public static int x; 
    public int x1; 

    public void function1(int x){
        Console.WriteLine({x});
        x1 = 200; 
        Console.WriteLine({x});

    }

    public void function2(ref int x){
      
      /*  Console.WriteLine(x);
        x1 = 300; 
        Console.WriteLine(x);
        */
    }
    public void function3(out int x){
      
      /*  Console.WriteLine(x);
        x = 400; 
        Console.WriteLine(x);
        */
    }

}