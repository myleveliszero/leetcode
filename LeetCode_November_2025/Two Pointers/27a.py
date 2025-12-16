from typing import *
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        for right in range(len(nums)):
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1
        return left
    
sol = Solution().removeElement
print(sol(nums = [0,1,2,2,3,0,4,2], val = 2))
print(sol(nums = [2,2,2,2,2,2,2,2], val = 2))
    
