using System;
using System.Collections.Generic;


     class CalculatorTesting
    {
        public static void Main(String[] args)
        {
            Console.WriteLine("-----------------  Calculator --------------------------");
            Console.WriteLine("########################################################");

            CalculatorFunctions operation = new CalculatorFunctions();

            Console.WriteLine("-----------------  Addition 1 --------------------------");

            Console.WriteLine("5.5 + 10 = " + (operation.Addition(5.5,10).ToString()));

            Console.WriteLine("-----------------  Addition 2 --------------------------");

            Console.WriteLine("-4.5 + 10 = " + (operation.Addition(-4.5, 10).ToString()));

            Console.WriteLine("-----------------  Subtraction 1 -----------------------");

            Console.WriteLine("-10 - 8 = " + (operation.Subtraction(-10, 8).ToString()));

            Console.WriteLine("-----------------  Subtraction 2 -----------------------");

            Console.WriteLine("100.5 - 20.5 = " + (operation.Subtraction(100.5,20.5).ToString()));

            Console.WriteLine("-----------------  Multiplication 1 --------------------");

            Console.WriteLine("20 * 50 = " + (operation.Multiplication(20,50).ToString()));

            Console.WriteLine("-----------------  Multiplication 2 --------------------");

            Console.WriteLine("-100 * 2.5 = " + (operation.Multiplication(-100, 2.5).ToString()));

            Console.WriteLine("-----------------  Division 1 --------------------------");
    
            Console.WriteLine("1 / 0 = " + operation.Division(1, 0).ToString()); 

            Console.WriteLine("-----------------  Division 2 --------------------------");

            Console.WriteLine("5 / (-15) = " + (operation.Division(5, -15).ToString()));

            Console.WriteLine("########################################################");
            Console.WriteLine("----------------- End of Calculator --------------------");

        }
    }
