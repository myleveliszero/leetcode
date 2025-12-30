from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(idx, subsets, curset):
            if idx >= len(nums):
                subsets.append(curset)
                return None
            backtrack(idx+1, subsets, curset.copy())
            curset.append(nums[idx])
            backtrack(idx+1, subsets, curset.copy())
        
        subsets, curset = [], []
        backtrack(0, subsets, curset)
        return subsets

    def subsets_2(self, nums: List[int]) -> List[List[int]]:
        def backtrack(idx, nums, subsets, curset):
            if idx >= len(nums):
                subsets.append(curset.copy())
                return None
            
            curset.append(nums[idx])
            backtrack(idx+1, nums, subsets, curset)
            curset.pop()
            backtrack(idx+1, nums, subsets, curset)
        
        subsets, curset = [], []
        backtrack(0, nums, subsets, curset)
        return subsets

sol = Solution().subsets_2
print(sol([1,2,3]))
