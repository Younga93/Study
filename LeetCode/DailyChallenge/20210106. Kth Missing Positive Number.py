'''
Given an array arr of positive integers sorted in a strictly increasing order,
and an integer k.
Find the kth positive integer that is missing from this array.

Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...].
             The 5th missing positive integer is 9.


Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...].
             The 2nd missing positive integer is 6.
'''

class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        answer = 0
        for num in arr:
            while num != None:
                answer += 1
                if num != answer:
                    k -= 1
                else:
                    break
                if k == 0:
                    return answer
        
        return answer + k


solution = Solution()
result = solution.findKthPositive([1,2,3,4], 2)
print(result)
