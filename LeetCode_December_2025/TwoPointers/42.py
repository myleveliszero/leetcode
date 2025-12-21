# from typing import List
# class Solution:
#     def trap(self, height: List[int]) -> int:
#         left = 0
#         while height[left] == 0: left += 1

#         water, right = 0, left+1

#         while right < len(height):
#             if height[right] >= height[left]:
#                 left = right
#                 right += 1
#             else:
#                 water = water + (height[left]-height[right])
#                 right += 1
        
#         return water
    
# sol = Solution().trap
# print(sol(height = [0,1,0,2,1,0,1,3,2,1,2,1]))

