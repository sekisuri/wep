using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CsharpConsole
{
    class Program
    {
        static void Main(string[] args)
        {
            //MyIndexer Indexer = new MyIndexer();
            char tmpCode = 'A';
            int codeAscii;
            MyIndexer Indexser = new MyIndexer();
            for(int i=0;i < 8; i++)
            {
                codeAscii = (int)tmpCode + i;
                Indexser[i] = "" + Convert.ToChar(codeAscii);
            }
            Indexser.Print();
            Indexser[1] = "Hello World";
            Indexser.Print();
        }
    }
}
