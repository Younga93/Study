using System;
using System.Collections.Generic;
using System.Collections;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Algorithm_csharp
{
    public class Solution
    {    
        // LeetCode - 1. Two Sum
        public int[] TwoSum(int[] nums, int target)
        {
            for (int i = 0; i < nums.Length; i++)
            {
                for (int j = i; j < nums.Length; j++)
                {
                    if (nums[i] + nums[j] == target)
                    {
                        return new int[] { i, j };
                    }
                }
            }
            return null;
        }
        // LeetCode - 7. Reverse Integer - Used string Conversion.
        public int Reverse(int x)
        {
            string num;
            string reversed;
            if (x < 0)
            {
                num = Convert.ToString(x * (-1));
                reversed = "-";
            }
            else
            {
                num = Convert.ToString(x);
                reversed = "";
            }
            for (int i = num.Length - 1; i >= 0; i--)
            {
                reversed += num.Substring(i, 1);
            }
            try
            {
                return Convert.ToInt32(reversed);
            }
            catch
            {
                return 0;
            }
        }
        // LeetCode - 9. Palindrome Number - Used string Conversion.
        public bool IsPalindrome(int x)
        {
            string str = Convert.ToString(x);

            int frontIndex = 0;
            int backIndex = str.Length - 1;
            

            while (true)
            {
                if (frontIndex >= backIndex)
                {
                    return true;
                }
                else if(str[frontIndex] == str[backIndex])
                {
                    frontIndex++;
                    backIndex--;
                    continue;
                }
                else
                {
                    return false;
                }
            }
        }
        // LeetCode - 13. Roman to Integer - Using Ditionary
        public int RomanToInt(string s)
        {
            int answer = 0;
            s += " ";
            char[] chars = s.ToCharArray();

            Dictionary<char, int> Roman = new Dictionary<char, int>();
            Roman.Add(' ', 0);
            Roman.Add('I', 1);
            Roman.Add('V', 5);
            Roman.Add('X', 10);
            Roman.Add('L', 50);
            Roman.Add('C', 100);
            Roman.Add('D', 500);
            Roman.Add('M', 1000);

            for (int i = 0; i < chars.Length - 1; i++)
            {
                if (Roman[chars[i + 1]] > Roman[chars[i]])
                {
                    answer -= Roman[chars[i]];
                    answer += Roman[chars[i + 1]];
                    i++;
                }
                else
                {
                    answer += Roman[chars[i]];
                }
            }
            return answer;
        }
        // LeetCode - 14. Longest Common Prefix
        public string LongestCommonPrefix(string[] strs)
        {
            if (strs.Length == 0)
            {
                return "";
            }

            string temp;
            for (int i = 0; i < strs[0].Length; i++)
            {
                temp = strs[0].Substring(i, 1);
                
                for (int j = 1; j < strs.Length; j++)
                {
                    if (strs[j].Length == i || temp != strs[j].Substring(i, 1))
                    {
                        return strs[0].Substring(0, i);
                    }
                }
            }
            return strs[0];
        }
        // LeetCode - 20. Valid Parentheses - Using Replace method
        public bool IsValid1(string s)
        {
            while (s.Contains("[]") || s.Contains("{}") || s.Contains("()"))
            {
                s = s.Replace("[]", "");
                s = s.Replace("{}", "");
                s = s.Replace("()", "");
            }

            if (s == "")
            {
                return true;
            }
            else
            {
                return false;
            }
        }
        // LeetCode - 20. Valid Parentheses - Using Stack
        public bool IsValid(string s)
        {
            if ( string.IsNullOrWhiteSpace(s) )
            {
                return false;
            }

            Stack<char> myStack = new Stack<char>();

            Dictionary<char, char> validSet = new Dictionary<char, char>();
            validSet.Add('{', '}');
            validSet.Add('[', ']');
            validSet.Add('(', ')');

            foreach (char l in s)
            {
                if (validSet.ContainsKey(l)) //(validSet.ContainsKey(l))
                {
                    myStack.Push(l);
                }
                else //not 0 // if (validSet.ContainsValue(l))
                {
                    if (myStack.Count != 0 && validSet[myStack.Peek()] == l)
                        myStack.Pop();
                    else
                        return false;
                }
            }

            return myStack.Count == 0 ? true : false;
        }
        // LeetCode - 21. Merge Two Sorted Lists
        public ListNode MergeTwoLists(ListNode l1, ListNode l2)
        {
            if (l1 == null)
                return l2;
            if (l2 == null)
                return l1;

            ListNode head = new ListNode();
            ListNode walk = head;
            while (true)
            {
                if (l1.val < l2.val)
                {
                    walk.next = l1;
                    l1 = l1.next;
                }
                else
                {
                    walk.next = l2;
                    l2 = l2.next;
                }
                walk = walk.next;

                if (l1 == null)
                {
                    walk.next = l2;
                    return head.next;
                }
                if (l2 == null)
                {
                    walk.next = l1;
                    return head.next;
                }
                
            }
        }
        // LeetCode - 26. Remove Duplicates from Sorted Array
        public int RemoveDuplicates(int[] nums)
        {
            if (nums.Length == 0)
                return 0;
            int index = 0;
            for (int i = 1; i < nums.Length; i++)
            {
                if (nums[index] != nums[i])
                {
                    nums[++index] = nums[i];
                }
            }
            return ++index; //Prefix increment because it requires the length of the array, not the index of the last element.
        }
    }
}
