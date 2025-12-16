# Status: Good

class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        answ = 0
        for i in range(1, min(a,b)+1):
            if a % i == 0 and b % i == 0:
                answ += 1
        return answ

solve = Solution()
print(solve.commonFactors(a = 12, b = 6))
print(solve.commonFactors(a = 25, b = 30))