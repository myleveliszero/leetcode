from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]
        for elem in nums:
            cperms = []
            for p in perms:
                for idx in range(len(p)+1):
                    p_copy = p.copy()
                    p_copy.insert(idx, elem)
                    cperms.append(p_copy)
            perms = cperms
        return perms 

    

sol = Solution().permute
print(sol([1,2,3]))
