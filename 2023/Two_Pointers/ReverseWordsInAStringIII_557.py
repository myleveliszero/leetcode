# Status: Good

class Solution:
    def reverseWords(self, s: str) -> str:
        res = ""
        l = 0
        for r in range(len(s)):
            if s[r] == " ":
                res += s[l:r][::-1] + " "
                l = r+1
        return res + s[l:len(s)][::-1]
    def simple(self, s ):
        return " ".join((s[::-1].split())[::-1])

solve = Solution()
print(solve.reverseWords(s = "Let's take LeetCode contest"))
print(solve.simple(s = "Let's take LeetCode contest"))