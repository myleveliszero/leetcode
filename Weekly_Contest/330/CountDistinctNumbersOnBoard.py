class Solution:
    def distinctIntegers(self, n: int) -> int:
        return n-1 if n != 1 else 1

solve = Solution()
print(solve.distinctIntegers(5))
print(solve.distinctIntegers(3))
print(solve.distinctIntegers(1))
