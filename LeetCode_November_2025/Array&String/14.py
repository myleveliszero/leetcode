from typing import *
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==1:
            return ""
        i = 0
        one, two = strs[0], strs[1]
        while i < len(one) and i < len(two) and one[i]==two[i]:
            i+=1

        str = strs[0][:i]
        
        
        for j in range(2, len(strs)):
            i = 0
            while i < len(str) and i < len(strs[j]) and str[i] == strs[j][i]:
                i += 1
            str = str[:i]
            if not str:
                return str

        return str            

sol = Solution().longestCommonPrefix

print(sol(strs = ["flower","flow","fli","fork","flow","flower","abc"]))
print(sol(strs = ["flower","flow","flight"]))