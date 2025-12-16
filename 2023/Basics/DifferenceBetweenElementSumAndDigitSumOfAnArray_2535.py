# Status: Not Bad

class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        element_sum = sum(nums)
        digit_sum = 0
        for i in nums:
            for j in str(i):
                digit_sum += int(j)
        return abs(digit_sum - element_sum)
        
solve = Solution()
print(solve.differenceOfSum([1,15,6,3]))