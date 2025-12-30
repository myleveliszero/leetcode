from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(idx, nums, subsets, curset, k):
            if idx >= len(nums):
                if len(curset) == k:
                    subsets.append(curset.copy())
                return 
            
            curset.append(nums[idx])
            backtrack(idx+1, nums, subsets, curset, k)
            curset.pop()
            backtrack(idx+1, nums, subsets, curset, k)

        nums = [i for i in range(1, n+1)]
        subsets, curset = [], []
        backtrack(0, nums, subsets, curset, k)
        return subsets
    
    def combine_2(self, n: int, k: int) -> List[List[int]]:
        def backtrack(val, n, subsets, curset, k):
            if val >= n+1:
                if len(curset) == k:
                    subsets.append(curset.copy())
                return 
            
            curset.append(val)
            backtrack(val+1, n, subsets, curset, k)
            curset.pop()
            backtrack(val+1, n, subsets, curset, k)

        subsets, curset = [], []
        backtrack(1, n, subsets, curset, k)
        return subsets

    def combine_3(self, n: int, k: int) -> List[List[int]]:
        def backtrack(val, n, subsets, curset, k):
            if len(curset) == k:
                subsets.append(curset.copy())
                return 
            if val > n:
                return 

            curset.append(val)
            backtrack(val+1, n, subsets, curset, k)
            curset.pop()
            backtrack(val+1, n, subsets, curset, k)

        subsets, curset = [], []
        backtrack(1, n, subsets, curset, k)
        return subsets
    
sol = Solution().combine
sol2 = Solution().combine_2
sol3 = Solution().combine_3
print(sol(4,2))
print(sol2(4,2))        
print(sol3(4,2))        