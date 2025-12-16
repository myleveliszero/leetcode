from typing import*
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left, max = 0, 0
        for right in range(1, len(nums)+1):
            if nums[right-1] == 1:
                if right - left > max:
                    max = right - left
            else:
                left = right
        return max
    
sol = Solution().findMaxConsecutiveOnes
print(sol(nums = [1,1,0,1,1,1]))
print(sol(nums = [1]))
print(sol(nums = [0]))
print(sol(nums = [0,0,0,0,0]))
print(sol(nums = [1,1,0,1,1,1,1,0,0,0,1,1,1]))
print(sol(nums = [0,0,0,0,1,1,1,1]))
print(sol(nums = [1,1,1,1,1,1]))
print(sol(nums = [0,1,0,1,0,1]))
print(sol(nums = [0,0,0,1,1,1,1,1,0,1,1,1]))
