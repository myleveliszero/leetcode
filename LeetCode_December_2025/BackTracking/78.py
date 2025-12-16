from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        global res
        res = []
        def backtrack(nums, lst, idx):
            if idx < len(nums):
                backtrack(nums, lst.copy(), idx+1)
                lst.append(nums[idx])
                backtrack(nums, lst.copy(), idx+1)
            else:
                res.append(lst)
                return None
        backtrack(nums, [], 0)
        return res 

sol = Solution().subsets
print(sol([1,2,3]))
