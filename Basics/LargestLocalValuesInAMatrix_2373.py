# Status: Good

class Solution:
    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
        glen = len(grid)
        outputlen = glen - 2
        pool_size = 3
        rows, cols = (outputlen, outputlen) 
        answ = [[0 for i in range(cols)] for j in range(rows)] 
        print(answ)
        for i in range(outputlen):
            for j in range(outputlen):
                curmax = 0
                for ii in range(i, pool_size+i):
                    for jj in range(j, pool_size+j):
                        if grid[ii][jj] > curmax:
                            curmax = grid[ii][jj]
                answ[i][j] = curmax
        return answ

solve = Solution()
print(solve.largestLocal([[20,8,20,6,16,16,7,16,8,10],[12,15,13,10,20,9,6,18,17,6],
[12,4,10,13,20,11,15,5,17,1],[7,10,14,14,16,5,1,7,3,11],
[16,2,9,15,9,8,6,1,7,15],[18,15,18,8,12,17,19,7,7,8],
[19,11,15,16,1,3,7,4,7,11],[11,6,5,14,12,18,3,20,14,6],
[4,4,19,6,17,12,8,8,18,8],[19,15,14,11,11,13,12,6,16,19]]))