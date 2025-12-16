from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(lst, idx, res):
            if idx >= len(nums):
                res.append(lst)
                return None
            backtrack(lst.copy(), idx+1, res)
            lst.append(nums[idx])
            backtrack(lst.copy(), idx+1, res)
        
        res = []
        backtrack([], 0, res)
        return res 

sol = Solution().subsets
print(sol([1,2,3]))
