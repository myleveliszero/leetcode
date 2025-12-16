from typing import *
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:    return False
        left, right= 0, len(arr)-1
        while right-1 > 0 and arr[right] < arr[right-1]:
            right -= 1
        while left+1 < len(arr) and arr[left] < arr[left+1]:
            left += 1
        return left==right
    

        
sol = Solution().validMountainArray

print(sol(arr = [0,2,3,4,5,2,1,0]))
print(sol(arr = [0,2,3,3,5,2,1,0]))
print(sol(arr = [0,0,0,0,1,1,1,1,3,2,1,1,0]))

print(sol(arr = [0,3,2,1]))
print(sol(arr = [2,1]))
print(sol(arr = [3,5,5]))