from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        csum, min_len = 0, len(nums)+1
        left = 0
        for right in range(len(nums)):
            csum += nums[right]
            while csum >= target and left < len(nums):
                if csum >= target:
                    min_len = min(min_len, right-left+1)
                csum -= nums[left]
                left += 1

        
        return min_len if min_len <= len(nums) else 0
    
    def minSubArrayLen_2(self, target: int, nums: List[int]):
        csum, min_len = 0, len(nums)+1
        left = 0
        for right in range(len(nums)):
            csum += nums[right]
            while csum >= target and left < len(nums):
                min_len = min(min_len, right-left+1)
                csum -= nums[left]
                left += 1
                
        return min_len % (len(nums)+1)
    
print(Solution().minSubArrayLen(target = 15, nums = [1,2,3,4,5]))
print(Solution().minSubArrayLen_2(target = 15, nums = [1,2,3,4,5]))