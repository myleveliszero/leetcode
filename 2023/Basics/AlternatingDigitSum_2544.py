# Status: Not Bad

class Solution:
    def alternateDigitSum(self, n: int) -> int:
        plus = True
        ans = 0
        for i in str(n):
            if plus:
                ans += int(i)
                plus = False
            else:
                ans -= int(i)
                plus = True
        return ans

solve = Solution()
print(solve.alternateDigitSum(886996))