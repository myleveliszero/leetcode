from typing import List
from random import randrange
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def QuickSortModified(nums, left, right):
            if right-left <= 0:
                return nums
            idx = randrange(left, right)
            nums[right], nums[idx] = nums[idx], nums[right]
            
            pivot = nums[right]
            lp = rp = left
            while rp < right:
                if nums[rp] < pivot:
                    nums[lp], nums[rp] = nums[rp], nums[lp]
                    lp += 1
                rp += 1
            
            lp = rp = left
            while rp < right:
                if nums[rp] <= pivot:
                    nums[lp], nums[rp] = nums[rp], nums[lp]
                    lp += 1
                rp += 1
            
            nums[lp], nums[right] = nums[right], nums[lp]
            llp = left
            while llp < lp:
                if nums[llp] == pivot:
                    break
                llp += 1


            QuickSortModified(nums, left, llp-1)
            QuickSortModified(nums, lp+1, right)

            return nums
        
        nums = QuickSortModified(nums, 0, len(nums)-1)
        return nums[-k]
    
print(Solution().findKthLargest([3,2,1,5,6,4], k=2))