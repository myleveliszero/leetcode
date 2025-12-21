from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left, counter = 1, 0 
        for right in range(1, len(nums)):
            if nums[left-1] != nums[right]:
                counter = 0
                nums[left] = nums[right]
                left += 1
            else:
                counter += 1
                if counter <= 1:
                    nums[left] = nums[right]
                    left += 1
        
        return left
    
    def removeDuplicates_2(self, nums: List[int]) -> int:
        if len(nums) < 3: return 2
        
        left = 2 
        for right in range(2, len(nums)):
            if nums[left-2] != nums[right]:
                nums[left] = nums[right]
                left += 1

        return left
    
    
    
print(Solution().removeDuplicates_2([0,0,1,1,1,1,2,3,3]))
print(Solution().removeDuplicates_2([1,1,1,2,2,3]))