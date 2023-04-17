# Status: Not Bad

class Solution:
    def rowAndMaximumOnes(self, mat: list[list[int]]) -> list[int]:
        ones = 0
        row = 0
        for i in range(len(mat)):
            sum_mat = sum(mat[i])
            if sum_mat > ones:
                ones = sum_mat
                row = i
        return [row, ones]
            
solve = Solution()
print(solve.rowAndMaximumOnes(mat = [[0,1],[1,0]]))
print(solve.rowAndMaximumOnes(mat = [[0,0,0],[0,1,1]]))