from typing import List
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(grid, row, col, lst):
            ROWS, COLS = len(grid), len(grid[0])
            if  min(row,col) < 0 or row==ROWS or col==COLS or grid[row][col] != 1:
                return 

            grid[row][col] = 0
            lst[0] += 1
            dfs(grid, row-1, col, lst)
            dfs(grid, row+1, col, lst)
            dfs(grid, row, col+1, lst)
            dfs(grid, row, col-1, lst)

        max_val = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    lst = [0]
                    dfs(grid, row, col, lst)
                    if lst[0] > max_val:
                        max_val = lst[0]

        return max_val


sol = Solution().maxAreaOfIsland


grid1 = [[1,1,1,1,1,0,1,1,1,1],
        [0,1,1,0,1,1,1,0,1,1],
        [1,0,1,0,1,1,0,1,0,1],
        [1,0,1,1,0,1,1,1,1,1],
        [1,1,0,0,1,1,1,1,1,1],
        [1,1,0,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,0,1],
        [0,1,1,0,1,1,1,1,1,0],
        [1,1,0,1,1,0,1,1,1,1],
        [0,1,1,1,1,1,0,1,1,1]]

grid2 = [
  [1,1,0,0,0],
  [1,1,0,0,0],
  [0,0,1,0,0],
  [0,0,0,1,1]
]
grid3 = [
  [1,1,1,1,0],
  [1,1,0,1,0],
  [1,1,0,0,0],
  [0,0,0,0,0]
]

grid4 = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]

# print(sol(grid1))
# print(sol(grid2))
# print(sol(grid3))
print(sol(grid4))