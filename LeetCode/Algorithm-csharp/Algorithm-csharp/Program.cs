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
            //Console.WriteLine(solution.IsValid("(])")); //F
            //Console.WriteLine(solution.IsValid("(]"));  //F
            //Console.WriteLine(solution.IsValid("()[]"));//T
            //Console.WriteLine(solution.IsValid("{[]}"));//T
            //Console.WriteLine(solution.IsValid("([)]"));//F

            ListNode l1 = new ListNode(1, new ListNode(2, new ListNode(4)));
            ListNode l2 = new ListNode(1, new ListNode(3, new ListNode(4)));

            DisplayList(solution.MergeTwoLists(l1,l2));
        }
        static void DisplayList(ListNode list)
        {
            Console.Write("[");
            while(list != null)
            {
                Console.Write(list.val + " ");
                list = list.next;
            }
            Console.Write("]");
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
