# Status: Good

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join((s[::-1]).split()[::-1])

solve = Solution()
print(solve.reverseWords(s = "Let's take LeetCode contest"))