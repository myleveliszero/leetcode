from typing import *
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroCnt = 0
        left, right = 0, 0
        while right < len(nums):
            if nums[right] == 0:
                zeroCnt += 1
                right += 1   
            else:
                nums[left] = nums[right]
                left, right = left+1, right+1      
        while zeroCnt > 0:
            nums[-zeroCnt] = 0
            zeroCnt -= 1

        return nums

sol = Solution().moveZeroes
print(sol(nums = [0,1,0,3,12]))