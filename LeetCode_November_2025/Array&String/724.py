from typing import *
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftsum, rightsum = 0, sum(nums)
        for i in range(len(nums)):
            rightsum -= nums[i]

            if rightsum == leftsum:
                return i
            leftsum += nums[i]
        return -1
                        

sol = Solution().pivotIndex
print(sol(nums = [1,7,3,6,5,6]))