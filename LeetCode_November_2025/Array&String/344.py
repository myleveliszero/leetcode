from typing import*
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i, j = 0, len(s)-1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i, j = i+1, j-1


sol = Solution().reverseString
print(sol(s = ["H","a","n","n","a","h"]))
print(sol(s = ["h","e","l","l","o"]))