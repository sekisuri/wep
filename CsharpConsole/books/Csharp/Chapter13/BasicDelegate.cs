using System;

namespace Delegate
{
    delegate int MyDelegate(int a, int b);
    
    class BasicDelegate
    {
        public int Plus(int a, int b)
        {
            return a + b;
        }    
        
        public static int Minus(int a, int b)
        {
            return a - b;
        }
    }
   
}