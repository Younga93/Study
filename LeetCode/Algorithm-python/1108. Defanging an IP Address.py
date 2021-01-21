class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        return address.replace(".", "[.]")

solution = Solution()
result = solution.defangIPaddr("1.1.1.1")
print(result)