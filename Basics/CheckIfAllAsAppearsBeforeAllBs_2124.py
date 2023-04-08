# Status: Not Bad

class Solution:
    def checkString(self, s: str) -> bool:
        return s == ''.join(sorted(s))
        #     return 'ba' not in s

solve = Solution()
print(solve.checkString(s = "aaabbb"))
print(solve.checkString(s = "bbb"))
print(solve.checkString(s = "aaa"))
print(solve.checkString(s = "abaa"))