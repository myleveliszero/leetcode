from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left, right = 0, 0 
        while right < len(nums):
            while nums[left] == nums[right]:
                right += 1
                if right >= len(nums):
                    break
            else:
                left += 1
                nums[left] = nums[right]
                right += 1
                
        return left+1
    


sol = Solution().removeDuplicates
# print(sol(nums = [1,1,2]))
print(sol(nums = [0,0,1,1,1,2,2,3,3,4,4,4,4]))  