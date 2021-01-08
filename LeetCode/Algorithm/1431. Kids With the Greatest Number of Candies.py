class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        Maximum_Candies = max(candies)
        answers = []
        for c in candies:
            if c + extraCandies >= Maximum_Candies:
                answers.append(True)
            else:
                answers.append(False)
        return answers


solution = Solution()

result = solution.kidsWithCandies([2,3,5,1,3], 3)

print(result)