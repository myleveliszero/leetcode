# Status: Good

class Solution:
    def replaceDigits(self, s: str) -> str:
        answ = ""
        for char in range(len(s)):
            if s[char] not in "0123456789":
                answ += s[char]
            else:
                answ += chr(ord(s[char-1])+int(s[char]))
        return answ

solve = Solution()
print(solve.replaceDigits(s = "a1c1e1"))