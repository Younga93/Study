class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        answer = list(s)
        
        index = 0
        for i in indices:
            answer[i] = s[index]
            index += 1

        return "".join(answer)

solution = Solution()

result = solution.restoreString("codeleet", [4,5,6,7,0,2,1,3])

print(result)