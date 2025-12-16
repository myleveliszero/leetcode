# Status: Not Bad

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: list[list[int]]) -> int:
        glen = len(grid)
        def colsrowsmaxes(matrix: list[list[int]], mlen: int) -> list[int]:
            maxcols, maxrows = [0]*mlen, [0]*mlen
            for i in range(0, mlen):
                for j in range(mlen):
                    if maxrows[i] < matrix[i][j]:
                        maxrows[i] = matrix[i][j]

                    if maxcols[j] < matrix[i][j]:
                        maxcols[j] = matrix[i][j]
            
            return maxcols, maxrows
        colsmaxes, rowsmaxes = colsrowsmaxes(grid, glen)
        answ = 0
        for i in range(glen):
            for j in range(glen):
                if rowsmaxes[i] > colsmaxes[j]:
                    answ += colsmaxes[j] - grid[i][j]
                else:
                    answ += rowsmaxes[i] - grid[i][j]

        return answ 

solve = Solution()
print(solve.maxIncreaseKeepingSkyline(grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]))
