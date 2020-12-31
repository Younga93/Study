class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        answer = 0
        length = len(nums)
        for i in range(length):
            for j in range(i, length):
                if nums[i] == nums[j] and i < j:
                    answer += 1
        return answer

solution = Solution()

result = solution.numIdenticalPairs([1,2,3,1,1,3])

print(result)