# Status: Good

class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return n if n%2 == 0 else 2*n
    def version2(self, n):
        return n << (n & 1)

solve = Solution()
print(solve.smallestEvenMultiple(14))
print(solve.version2(14))