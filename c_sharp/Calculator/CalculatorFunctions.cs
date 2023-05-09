using System;
using System.Collections.Generic;


     class CalculatorFunctions
    {
        private double result;

        // ------------------ Addition ----------------------//
        public double Addition(double num1, double num2)
        {
            this.result = num1 + num2;  // all real numbers can be added
            return this.result; 
        }

        // ------------------ Subtraction ----------------------//
        public double Subtraction(double num1, double num2)
        {
            this.result = num1 - num2; // all real numbers can be subtracted
            return this.result; 
        }
        // ------------------ Multiplication ----------------------//
        public double Multiplication(double num1, double num2)
        {
            this.result = num1 * num2; // all real numbers can be multiplied
            return this.result;
        }
        // ------------------ Division ----------------------//
        public double Division(double num1, double num2)
        {
           if(num2 == 0) // division by zero is not allowed
            {
                Console.WriteLine("Can NOT divide by Zero");
                return Double.NaN; 
            }
            this.result = num1 / num2;
            return this.result; 
        }
    }
