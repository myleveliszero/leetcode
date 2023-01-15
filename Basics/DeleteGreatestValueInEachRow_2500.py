# Status: Not Bad

class Solution:
    def deleteGreatestValue(self, grid: list[list[int]]) -> int:
        answ = 0
        for  col in range(len(grid[0])):
            rowmaxes = []
            for row in range(len(grid)):
                curmax = max(grid[row])
                grid[row].remove(curmax)
                rowmaxes.append(curmax)
            answ += max(rowmaxes)
        return answ


solve = Solution()
print(solve.deleteGreatestValue(grid = [[1,2,4],[3,3,1]]))
