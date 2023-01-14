# Status: Good

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        answ = start
        for i in range(1, n):
            answ ^= start + 2 * i
        return answ

solve = Solution()
print(solve.xorOperation(n = 5, start = 0))
print(solve.xorOperation(n = 4, start = 3))