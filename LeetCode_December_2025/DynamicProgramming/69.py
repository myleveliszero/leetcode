class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1]*n, [1]*n]
        for _ in range(m-1):
            for j in reversed(range(n-1)):
                dp[1][j] = dp[1][j+1]+dp[0][j]
            dp[1], dp[0] = dp[0], dp[1]
        
        return dp[0][0]




sol = Solution().uniquePaths
print(sol(3, 7))


def uniquePaths(m: int, n: int) -> int:
    def memoization(row, col, rows, cols, memo):
        if row == rows or col == cols:
            return 0
        if memo[row][col] != 0:
            return memo[row][col]
        if row == rows-1 and col == cols-1:
            return 1
        
        memo[row][col] = (memoization(row+1, col, rows, cols, memo) + 
                            memoization(row, col+1, rows, cols, memo))

        return memo[row][col]

    memo = [[0]*n for _ in range(m)]
    return memoization(0,0, m, n, memo)


from random import randrange as rd

def test(func1, func2):
    m, n = rd(1,10), rd(1,10)
    # print(m,n)
    res1 = func1(m,n)
    res2 = func2(m,n)
    if res1 != res2:
        print(m,n)
        return 
    
for i in range(100):
    test(sol, uniquePaths)