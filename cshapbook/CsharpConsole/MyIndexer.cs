using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CsharpConsole
{
    class MyIndexer
    {
        string[] storage = new string[3];
        public string this[int index]
        {
            get
            {
                return storage[index];
            }
            set
            {
                storage[index] = value;
            }
        }
        public string this[string key] //문자열을 인자로 받는 인덱서
        {
            get
            {
                return storage[1];
            }
            set
            {
                storage[1] = value;
            }
        }



    }
}
