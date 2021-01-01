class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        answer = len(words)

        for word in words:
            for l in word:
                if l not in allowed:
                    answer -= 1
                    break
        return answer

solution = Solution()

result = solution.countConsistentStrings("ab", ["ad","bd","aaab","baa","badab"])

print(result)