class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i, j = 0, 0
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i, j = i+1, j+1
                if j == len(needle):
                    return i-j
            else:
                i, j = i-j+1, 0    
        return -1


    
sol = Solution().strStr
print(sol("mississippi", "issip"))
print(sol(haystack = "leetcode", needle = "leeto"))