from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(grid, row, col):
            ROWS, COLS = len(grid), len(grid[0])
            if  min(row, col) < 0 or row == ROWS or col  == COLS or grid[row][col] != '1':
                return            
            
            grid[row][col] = '0'
            dfs(grid, row-1, col)
            dfs(grid, row+1, col)
            dfs(grid, row, col-1)
            dfs(grid, row, col+1)
            return 

        ans = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    dfs(grid, row, col)
                    ans += 1

        return ans

sol = Solution().numIslands


grid1 = [["1","1","1","1","1","0","1","1","1","1"],
        ["0","1","1","0","1","1","1","0","1","1"],
        ["1","0","1","0","1","1","0","1","0","1"],
        ["1","0","1","1","0","1","1","1","1","1"],
        ["1","1","0","0","1","1","1","1","1","1"],
        ["1","1","0","1","1","1","1","1","1","1"],
        ["1","1","1","1","1","1","1","1","0","1"],
        ["0","1","1","0","1","1","1","1","1","0"],
        ["1","1","0","1","1","0","1","1","1","1"],
        ["0","1","1","1","1","1","0","1","1","1"]]

grid2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
grid3 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

print(sol(grid1))
print(sol(grid2))
print(sol(grid3))

        