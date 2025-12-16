from typing import *
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])

sol = Solution().reverseWords
# print(sol(s = "            the sky is blue             "))
print(sol(s = "   hello      world                               "))
print(sol(s ="a       good   example"))