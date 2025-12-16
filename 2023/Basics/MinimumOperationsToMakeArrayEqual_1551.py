# Status: Bad

class Solution:
    def minOperations(self, n: int) -> int:
        return n*n//4

solve = Solution()
print(solve.minOperations(6))