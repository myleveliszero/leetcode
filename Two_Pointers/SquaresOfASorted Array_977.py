# Status: Good

# Two technique exist for two_pointers:
# 1. Start, End
# 2. Slow, Fast

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        left, right = 0, len(nums)-1
        ans = [0]*len(nums)
        for idx in range(len(nums)-1, -1, -1):
            if (abs(nums[right]) > abs(nums[left])):
                ans[idx] = nums[right]*nums[right]
                right -= 1
            else:
                ans[idx] = nums[left]*nums[left]
                left += 1
        return ans
        
    def simple(self, nums):
        return sorted([i**2 for i in nums])

solve = Solution()
print(solve.sortedSquares(nums = [-4,-1,0,3,10]))
print(solve.sortedSquares(nums = [-7,-3,2,3,11]))
print(solve.sortedSquares(nums = [-4,-2,-1,0,2,3,10]))