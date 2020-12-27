class Solution:
    def maximumWealth(self, accounts):
        answer = 0
        current_customer = 0
        for customer in accounts:
            current_customer = sum(customer)
            if current_customer > answer:
                answer = current_customer
            current_customer = 0
        return answer
        


solution = Solution()

result = solution.maximumWealth([[1,2,3],[3,2,1]])

print(result)