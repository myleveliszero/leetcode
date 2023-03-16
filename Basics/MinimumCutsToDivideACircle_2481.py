# Status: Good

class Solution:
    def numberOfCuts(self, n: int) -> int:
        if n == 1:
            return 0
        elif n % 2 == 0:
            return n//2
        else:
            return n
            
solve = Solution()
print(solve.numberOfCuts(99))
print(solve.numberOfCuts(66))
print(solve.numberOfCuts(1))
print(solve.numberOfCuts(4))
print(solve.numberOfCuts(3))