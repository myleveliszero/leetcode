class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([word[::-1] for word in s.split()])
    
sol = Solution().reverseWords
# print(sol(s = "            the sky is blue             "))
print(sol(s = "   hello      world                               "))
print(sol(s ="a       good   example"))