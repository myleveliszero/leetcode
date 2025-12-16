# Status: Not Bad

class Solution:
    def numberToBase(self, n, b):
        if n == 0:
            return [0]
        digits = []
        while n:
            digits.append(int(n % b))
            n //= b
        return digits[::-1]
    def sumBase(self, n: int, k: int) -> int:
        n = self.numberToBase(n,k)
        answ = 0
        for i in n:
            answ += int(i)
        return answ

solve = Solution()
print(solve.sumBase(n = 34, k = 6))
print(solve.sumBase(n = 10, k = 10))