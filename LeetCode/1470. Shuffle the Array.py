class Solution:
    def shuffle(self, nums, n):
        answer = []
        for x in range(n):
            answer.append(nums[x])  # append x element
            answer.append(nums[x+n])    # append y element
        return answer


solution = Solution()

result = solution.shuffle([2,5,1,3,4,7],3)

print(result)