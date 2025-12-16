# Status: Good

class Solution:
    def numberOfSteps(self, num: int) -> int:
        answ = 0
        while num:
            if num % 2 == 0:
                num //=2
            else:
                num -= 1
            answ += 1
        return answ

solve = Solution()
print(solve.numberOfSteps(99))