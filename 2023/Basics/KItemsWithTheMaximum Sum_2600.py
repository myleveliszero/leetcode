# Status: Not Bad

class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        ans = 0
        for i in range(k):
            if numOnes != 0:
                ans += 1
                numOnes -= 1
            elif numZeros != 0:
                numZeros -= 1
            elif numNegOnes != 0:
                ans -= 1
                numNegOnes -= 1
        return ans

solve = Solution()
print(solve.kItemsWithMaximumSum(numOnes = 3, numZeros = 2, numNegOnes = 0, k = 2))
print(solve.kItemsWithMaximumSum(numOnes = 3, numZeros = 2, numNegOnes = 0, k = 4))