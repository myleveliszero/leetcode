from typing import *
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:    return False

        peakOfMnt = False 
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                peakOfMnt = i
                break
        if not peakOfMnt:
            return False               
        
        for j in range(peakOfMnt):
            if arr[j] >= arr[j+1]:
                return False
        
        for k in range(peakOfMnt+1, len(arr)-1):
            if arr[k] <= arr[k+1]:
                return False

        return True
        
sol = Solution().validMountainArray

print(sol(arr = [0,2,3,4,5,2,1,0]))
print(sol(arr = [0,2,3,3,5,2,1,0]))
print(sol(arr = [0,0,0,0,1,1,1,1,3,2,1,1,0]))

print(sol(arr = [0,3,2,1]))
print(sol(arr = [2,1]))
print(sol(arr = [3,5,5]))