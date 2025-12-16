from typing import *
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max = arr[-1]
        for i in range(len(arr)-1, 0,-1):
            if max >= arr[i-1]:
                arr[i-1] = max
            else:
                temp = arr[i-1]
                arr[i-1] =  max
                max = temp
                
        arr[-1] = -1
        return arr
    
sol = Solution().replaceElements
print(sol([17,18,5,4,6,1]))
print(sol([17,18,5,4,6,6,6,6,6,7]))