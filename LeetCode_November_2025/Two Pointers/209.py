from typing import* 
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        left, right, curSum, minLenSub = 0, 0, 0, len(nums)
        while right < len(nums):
            if nums[right] >= target:
                return 1
            if curSum < target:
                curSum += nums[right]
                right += 1
            while curSum >= target:
                if minLenSub > right-left:
                    minLenSub = right-left
                curSum -= nums[left]
                left += 1

        return minLenSub



sol = Solution().minSubArrayLen
# print(sol(target = 150, nums = [2,3,1,2,4,3]))
print(sol(target = 11, nums = [1,2,3,4,5]))
print(sol(213, [12,28,83,4,25,26,25,2,25,25,25,12]))
print(sol(target = 7, nums = [2,3,1,2,4,3]))
print(sol(target = 4, nums = [1,4,4]))
