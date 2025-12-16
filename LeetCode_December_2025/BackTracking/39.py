# from typing import List
# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         global res
#         res = []        
#         def back(lst, lst_sum, idx):
#             if lst_sum == target:
#                 res.append(lst)
#                 return None
#             if idx >= len(candidates):
#                 return None

#             back(lst.copy(), lst_sum, idx+1)
#             lst_sum += candidates[idx]
#             lst.append(candidates[idx])
#             back(lst.copy(), lst_sum, idx+1)

#         back([], 0, 0)

#         return res

# sol = Solution().combinationSum
# print(sol(candidates = [2,3,6,7], target = 7))