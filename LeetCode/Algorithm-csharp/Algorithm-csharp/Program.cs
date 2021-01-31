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

            //ListNode l1 = new ListNode(1, new ListNode(2, new ListNode(4)));
            //ListNode l2 = new ListNode(1, new ListNode(3, new ListNode(4)));

            //DisplayList(solution.MergeTwoLists(l1,l2));

            //Display Array
            //Console.WriteLine(String.Join(",", new int[] { 1,2,3,4,5}));

            //Console.WriteLine("{0}",solution.RemoveDuplicates(new int[] {1,1,2}));

            //int[] nums = new int[] { 3, 2, 2, 3 };
            //Console.WriteLine("{0}",solution.RemoveElement(nums, 3));
            //Console.WriteLine(String.Join(", ", nums));
            string haystack = "";
            string needle = "a";
            Console.WriteLine(solution.StrStr(haystack, needle));
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
    }
}
