using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CsharpConsole
{
   
    class ExamClass
    {
        public void PrintA(string msg)
        {
            Console.WriteLine(msg);
        }
        public void PrintB(string msg)
        {
            Console.WriteLine(msg);
        }
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
            ExamClass cat = new ExamClass();

            // 옛날 델리게이트 이벤트 선언방식 C# 1.0 이하
            exam.EventHandler += new EventDelegate(cat.PrintA);
            exam.EventHandler += new EventDelegate(cat.PrintB);
            exam.EventFuntion("Good!!");

            // 최근의 델리게이트 이벤트 선언방식 C# 2.0 이상
            exam.EventHandler -= cat.PrintB;
            exam.EventFuntion("Hi!");

            exam.EventHandler -= cat.PrintA;
            //exam.EventFuntion("Hello~`");

            exam.EventHandler += cat.PrintA;
            exam.EventHandler += cat.PrintA;
            exam.EventFuntion("hello~`");
        }
    }
}
