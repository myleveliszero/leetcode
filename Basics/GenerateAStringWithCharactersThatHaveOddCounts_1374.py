# Status: Good

class Solution:
    def generateTheString(self, n: int) -> str:
        return 'z'*(n-1) + 'x' if n % 2 == 0 else 'c'*n

solve = Solution()
print(solve.generateTheString(8))
print(solve.generateTheString(9))
print(solve.generateTheString(11))