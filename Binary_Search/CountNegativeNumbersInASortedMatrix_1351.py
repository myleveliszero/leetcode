# Status: Good

class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        cnt = 0
        for oneD in grid:
            left, right = 0, len(oneD)-1
            while left <= right:
                mid = left + (right-left)//2
                if oneD[mid] <= -1:
                    right = mid-1
                else:
                    left = mid+1
            cnt += len(oneD) - left
        return cnt
    def version2(self, grid):
        m, n = len(grid), len(grid[0])
        cnt, row, col = 0, m-1, 0
        while row >= 0 and col < n:
            if grid[row][col] < 0:
                cnt += n - col
                row -= 1
            else:
                col += 1
        return cnt 


solve = Solution()
print(solve.countNegatives(grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))

print(solve.version2(grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))
