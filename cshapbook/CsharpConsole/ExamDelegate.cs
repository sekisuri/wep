using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CsharpConsole
{
    delegate void DelegateType(string str);
    // 멀티캐스트 델리게이트 
    delegate void MulitDelegate();
    // 이벤트 델리게이트
    delegate void EventDelegate(string Message);
    

    class ExamDelegate
    {
        // 이벤트 델리게이트는 클래스 내부에 선언
        public event EventDelegate EventHandler;

        public void EventFuntion(string msg)
        {
            EventHandler(msg);
        }
        public void DelegatePrint(string str)
        {
            Console.WriteLine(str);
        }
        public void Multi1Print()
        {
            Console.WriteLine("MultiPrint 1st");
        }
        public void Multi2Print()
        {
            Console.WriteLine("Second MultiPrint");
        }
       
    }
}
