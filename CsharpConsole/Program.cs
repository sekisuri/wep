using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CsharpConsole
{
    class Cat
    {
        
        public string Color;

        public void Meow(string Name)
        {
            Console.WriteLine("{0} : 야옹", Name);
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            ExamDelegate exam = new ExamDelegate();
            DelegateType Method1 = new DelegateType(exam.DelegatePrint);
            Method1("Hello World");

            Cat cat = new Cat();
            DelegateType CatMethod = new DelegateType(cat.Meow);
            CatMethod("깜장 고양이");

            DelegateType Method2 = cat.Meow;
            CatMethod("하양 고양이");
            
        }
    }
}
