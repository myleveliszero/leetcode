# Status: Good

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        max1 = max2 = float('-inf')
        for n in nums:
            if n >= max1:
                max1, max2 = n, max1
            elif n > max2:
                max2 = n
        return (max1-1)*(max2-1)

solve = Solution()
print(solve.maxProduct(nums = [3,4,5,2]))
print(solve.maxProduct(nums = [3,4,1,3,4,6,8,9,1,2,4,10,5,2]))