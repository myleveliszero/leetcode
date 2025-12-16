# Status: Not Bad

class Solution:
    def sumZero(self, n: int) -> list[int]:
        ans = []
        for i in range(n//2):
            ans.append(i+1)
            ans.append(~i)
        if n % 2 == 1:
            ans.append(0)
        return ans

    
solve = Solution()
print(solve.sumZero(n = 5))
print(solve.sumZero(n = 1))