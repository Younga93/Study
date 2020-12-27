class Solution:
    def maximumWealth(self, accounts):
        accounts = [sum(wealth) for wealth in accounts]
        return max(accounts)

solution = Solution()

result = solution.maximumWealth([[1,2,3],[3,2,1]])

print(result)