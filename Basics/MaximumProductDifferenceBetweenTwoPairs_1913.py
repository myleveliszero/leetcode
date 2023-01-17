# Status: 

class Solution:
    def maxProductDifference(self, nums: list[int]) -> int:
        # maximazed((a * b) - (c * d))
        nums.sort()
        return nums[-1]*nums[-2] - nums[0]*nums[1]
    def version2(self, nums):
        min1 = min2 = float('inf')
        max1 = max2 = float('-inf')
        for n in nums:
            if n <= min1:
                min1, min2 = n, min1
            elif n < min2:
                min2 = n
            if n >= max1:
                max1, max2 = n, max1
            elif n > max2:
                max2 = n
        return max1*max2 - min1*min2



solve = Solution()
print(solve.maxProductDifference(nums = [5,6,2,7,4]))
print(solve.version2(nums = [5,6,2,7,4]))