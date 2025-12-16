# Status: Good

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        left, right = 0, len(nums)-1
        while left <= right:
            if nums[left] + nums[right] == target:
                return [left+1, right+1]
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                left += 1

        return [-1,-1]
    
solve  = Solution()
print(solve.twoSum(nums = [2,7,11,15], target = 9))

print(solve.twoSum(nums = [2,3,4], target = 6))