# Status: Good

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0]) 
        for oneD in matrix:
            left, right = 0 , n-1
            while left <= right:
                mid = left + (right-left)
                if oneD[mid] == target:
                    return True
                elif oneD[mid] < target:
                    left = mid+1
                else:
                    right = mid-1
        
        return False        

    def version2(self, matrix, target):
        """
        n * m matrix convert to an array => matrix[x][y] => a[x * m + y]
        an array convert to n * m matrix => a[x] =>matrix[x / m][x % m];
        """
        m, n = len(matrix), len(matrix[0]) 
        left, right = 0, m*n - 1
        while left <= right:
            mid = left + (right - left)//2
            istarget = matrix[mid // n][mid % n]
            if istarget == target:
                return True
            elif istarget < target:
                left = mid+1
            else:
                right = mid-1
        return False


solve = Solution()
print(solve.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3))
print(solve.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13)) 