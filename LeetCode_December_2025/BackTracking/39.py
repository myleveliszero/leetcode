from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def back(lst, lst_sum, idx, res):
            if lst_sum == target:
                res.append(lst)
                return None
            if idx >= len(candidates):
                return None
            if lst_sum > target:
                return None
            
            new_lst = lst.copy()
            new_lst.append(candidates[idx])
            new_lst_sum = lst_sum + candidates[idx]
            back(new_lst.copy(), new_lst_sum, idx, res)
            
            back(lst.copy(), lst_sum, idx+1, res)

        res = []
        back([], 0, 0, res)

        return res

sol = Solution().combinationSum
print(sol(candidates = [2,3,6,7], target = 7))