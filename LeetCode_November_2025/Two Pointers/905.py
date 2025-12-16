from typing import *
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums)-1 
        while left < right:
            if nums[left] % 2 == 0:
                left += 1
            elif nums[left] % 2 != 0 and nums[right] % 2 == 0:
                nums[left], nums[right] = nums[right], nums[left]
                left, right = left+1,right-1
            
            elif nums[left] % 2 != 0 and nums[right] % 2 != 0:
                right -= 1
        
        return nums

sol = Solution().sortArrayByParity
print(sol(nums = [3,1,2,4]))
print(sol(nums = [3]))