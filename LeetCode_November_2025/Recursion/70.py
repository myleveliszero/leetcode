class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2: 
            return 1 if n==1 else 2
        prev, prev_prev = 2, 1
        for _ in range(3, n+1):
            cur = prev+prev_prev
            prev, prev_prev = cur, prev
        return cur

sol = Solution().climbStairs
print(sol(5))
