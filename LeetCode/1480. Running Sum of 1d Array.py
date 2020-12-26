class Solution:
    def runningSum(self, nums):
        answer = []
        current_sum = 0

        for x in nums:
            current_sum += x
            answer.append(current_sum)
        
        return answer


solution = Solution()

result = solution.runningSum([1, 2, 3, 4])

print(result)