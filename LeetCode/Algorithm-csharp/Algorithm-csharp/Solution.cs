using System;
using System.Collections.Generic;
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
        // LeetCode - 7. - Used string Conversion.
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
    }
}
