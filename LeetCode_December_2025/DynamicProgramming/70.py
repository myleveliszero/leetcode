class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 4: return n
        dp = [1,2]
        for _ in range(3, n+1):
            dp[1], dp[0] = dp[1]+dp[0], dp[1]
        return dp[1]
    
print(Solution().climbStairs(10))