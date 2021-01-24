using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Algorithm_csharp
{
    class Program
    {
        static void Main(string[] args)
        {
            Solution solution = new Solution();
            string[] strs = {"flower", "flow", "flight"};
            Console.WriteLine(solution.LongestCommonPrefix(strs));
        }

        static void DisplayArray(int[] array)
        {
            if (array == null)
            {
                Console.WriteLine("null");
            }
            else
            {
                Console.Write("{");
                for (int i = 0; i < array.Length; i++)
                {
                    if (i == array.Length - 1)
                        Console.Write(array[i]);
                    else
                        Console.Write(array[i] + ", ");
                }
                Console.WriteLine("}");
            }
        }
    }
}
