class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {1:1, 2:2, 3:3}
        def recur(n, memo=None):
            if n in memo: 
                return memo[n]
            memo[n] = recur(n-1, memo)+recur(n-2, memo)
            return memo[n]  
        return recur(n, memo)

sol = Solution().climbStairs
print(sol(5)) 



