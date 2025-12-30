from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(val, n, combs, curCombs, k):
            if len(curCombs) == k:
                combs.append(curCombs.copy())
                return
            if val > n:
                return  

            for i in range(val, n+1):
                curCombs.append(i)
                backtrack(i+1, n, combs, curCombs, k) 
                curCombs.pop()           
            
        subsets, curset = [], []
        backtrack(1, n, subsets, curset, k)
        return subsets
    
sol = Solution().combine
print(sol(4,2))