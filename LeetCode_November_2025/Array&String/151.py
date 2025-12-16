from typing import *
class Solution:
    def reverseWords(self, s: str) -> str:
        def lstrip(str):
            i = 0
            while str[i] == " ":
                i+=1
            return str[i:]
        def rstrip(str):
            i = len(str)-1
            while str[i] == " ":
                i -= 1
            return str[:i+1] 
        
        def mStripAndSplit(str):
            i = 0
            res = []
            while i < len(str):
                if str[i] != " ":
                    word = ""
                    while i < len(str) and str[i] != " ":
                        word += s[i]
                        i += 1
                    res.append(word)
                else:
                    i += 1
            return res

        s = lstrip(s)
        s = rstrip(s)
        lst = mStripAndSplit(s)
        lst = lst[::-1]
        return " ".join(lst)

sol = Solution().reverseWords
# print(sol(s = "            the sky is blue             "))
print(sol(s = "   hello      world                               "))
print(sol(s ="a       good   example"))