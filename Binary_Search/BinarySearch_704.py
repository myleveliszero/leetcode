# Status: Good

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        nlen = len(nums)
        left, right = 0, nlen-1
        while left <= right:
            i = (left+right)//2
            if nums[i] == target:
                return i
            elif nums[i] < target:
                left = i + 1
            else:
                right = i - 1
        return -1        
    
solve = Solution()
print(solve.search(nums = [5], target = 5))
print(solve.search(nums = [-5,3], target = 3))
print(solve.search(nums = [-1,0,3,5,9,12], target = 9))
print(solve.search(nums = [-1,0,3,5,9,12], target = 2))
