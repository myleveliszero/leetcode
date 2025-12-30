from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(idx, nums, perms, curperm, curset):
            if idx >= len(nums):
                perms.append(curperm.copy())
                return 
            
            for i in range(len(nums)):
                if nums[i] not in curset:     
                    curset.add(nums[i])
                    curperm.append(nums[i])
                    backtrack(idx+1, nums, perms, curperm, curset)
                    curset.remove(nums[i])
                    curperm.pop()
                
            return 

        perms, curperm, curset = [],[], set() 
        backtrack(0, nums, perms, curperm, curset)
        return perms
    
    def permute_2(self, nums: List[int]) -> List[List[int]]:
        def backtrack(idx, nums):
            if idx >= len(nums):
                return [[]]
            
            perms = backtrack(idx+1, nums)
            res = []
            for perm in perms:
                for i in range(len(perm)+1):
                    new_perm = perm.copy()
                    new_perm.insert(i, nums[idx])
                    res.append(new_perm)

            return res
            
        perms = backtrack(0, nums)  
        return perms
    

sol = Solution().permute
sol2 = Solution().permute_2
print(sol([1,2,3]))
print(sol2([1,2,3]))
