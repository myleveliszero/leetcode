from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(idx, nums, subsets, curset):
            if idx >= len(nums):
                subsets.append(curset.copy())
                return 
            
            curset.append(nums[idx])
            backtrack(idx+1, nums, subsets, curset)
            curset.pop()

            while idx+1 < len(nums) and nums[idx] == nums[idx+1]:
                idx += 1

            backtrack(idx+1, nums, subsets, curset)

        nums.sort()
        subsets, curset = [], []
        backtrack(0, nums, subsets, curset)
        return subsets
    
sol = Solution().subsetsWithDup
print(sol([3,1,2,2]))