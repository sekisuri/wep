using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CsharpConsole
{
    delegate void DelegateType(string str);
    /// <summary>
    /// <c> 멀티캐스트 델리게이트</c>
    /// </summary>

    class ExamDelegate
    {
        /// <summary>
        /// 
        /// </summary>
        /// <param name="str"></param>
        public void DelegatePrint(string str)
        {
            Console.WriteLine(str);
        }
       
    }
}
