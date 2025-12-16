from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def findIdx(grid):
            for row in range(len(grid)):
                for col in range(len(grid[0])):
                    if grid[row][col] == '1':
                        return (row, col)
            return -1 

        def traverse(grid, row, col):
            ROWS, COLS = len(grid), len(grid[0])
            if  min(row, col) < 0 or \
                row == ROWS or col  == COLS or \
                grid[row][col] == '0':
                return            
            if grid[row][col] == '1':
                grid[row][col] = '0'

            traverse(grid, row-1, col)
            traverse(grid, row+1, col)
            traverse(grid, row, col-1)
            traverse(grid, row, col+1)
            return 

        island_idx = findIdx(grid)
        count = 0
        while island_idx != -1:
            count += 1
            traverse(grid, island_idx[0], island_idx[1])
            island_idx = findIdx(grid)
        
        return count

sol = Solution().numIslands


grid = [["1","1","1","1","1","0","1","1","1","1"],
        ["0","1","1","0","1","1","1","0","1","1"],
        ["1","0","1","0","1","1","0","1","0","1"],
        ["1","0","1","1","0","1","1","1","1","1"],
        ["1","1","0","0","1","1","1","1","1","1"],
        ["1","1","0","1","1","1","1","1","1","1"],
        ["1","1","1","1","1","1","1","1","0","1"],
        ["0","1","1","0","1","1","1","1","1","0"],
        ["1","1","0","1","1","0","1","1","1","1"],
        ["0","1","1","1","1","1","0","1","1","1"]]

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

print(sol(grid))

        