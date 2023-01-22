# Status: Good

class Solution:
    def minOperations(self, nums: list[int]) -> int: 
        answ = 0
        for i in range(len(nums)-1):
            if nums[i] >= nums[i+1]:
                answ += nums[i] - nums[i+1] + 1
                nums[i+1] = nums[i] + 1
        return answ
    
    def version2(self, nums):
        answ = prev = 0
        for cur in nums:
            if cur <= prev:
                prev += 1
                answ += prev - cur
            else:
                prev = cur
        return answ



solve = Solution()
print(solve.minOperations(nums = [1,1,1]))
print(solve.minOperations(nums = [1,5,2,4,1]))
print(solve.version2(nums = [1,1,1]))
print(solve.version2(nums = [1,5,2,4,1]))