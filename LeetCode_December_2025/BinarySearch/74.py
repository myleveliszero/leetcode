from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_left, row_right = 0, len(matrix)-1
        col_left, col_right = 0, len(matrix[0])-1
        while row_left <= row_right:
            row_mid = row_left+(row_right-row_left)//2
            if matrix[row_mid][0] > target:
                row_right = row_mid-1
            else:
                row_left = row_mid+1
        
        while col_left <= col_right:
            col_mid = col_left+(col_right-col_left)//2 
            val = matrix[row_right][col_mid]
            if  val == target:
                return True
            if val > target:
                col_right = col_mid-1
            else:
                col_left = col_mid+1
        return False

                
print(Solution().searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 1))
print(Solution().searchMatrix(matrix = [[1],
                                        [3]], target = 1))
print(Solution().searchMatrix(matrix = [[1,2],
                                        [3,4]], target = 2))