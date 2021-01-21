class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = []

        for i in range(len(nums)):
            counter = 0
            for j in range(len(nums)):
                if i == j:
                    continue
                else:
                    if nums[i] > nums[j]:
                        counter += 1
            answer.append(counter)
        
        return answer

solution = Solution()

result = solution.smallerNumbersThanCurrent([8,1,2,2,3])

print(result)