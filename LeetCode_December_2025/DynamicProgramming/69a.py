class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
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


sol = Solution().uniquePaths
print(sol(3, 3))


def brute_force(row, col, rows, cols):
    if row == rows or col == cols:
        return 0
    if row == rows-1 and col == cols-1:
        return 1
    
    return (brute_force(row+1, col, rows, cols)+
            brute_force(row, col+1, rows, cols))

from random import randrange as rd

def test(func1, func2):
    m, n = rd(1,10), rd(1,10)
    res1 = func1(m,n)
    res2 = func2(0,0,m,n)
    # print(m,n)
    if res1 != res2:
        return 
    
for i in range(100):
    test(sol, brute_force)