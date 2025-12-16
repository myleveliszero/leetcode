from typing import List
from random import randrange

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def MergeSort(nums, left, right):
            if right-left <= 0:
                return nums[left:right+1]
            i = (right+left)//2
            part1 = MergeSort(nums, left, i)
            part2 = MergeSort(nums, i+1, right)
            new_arr = []
            lp, rp = 0, 0 # lp=leftpointer
            while lp < len(part1) and rp < len(part2):
                if part1[lp] <= part2[rp]:
                    new_arr.append(part1[lp])
                    lp += 1
                else:
                    new_arr.append(part2[rp])
                    rp += 1
            while lp < len(part1): 
                new_arr.append(part1[lp]); 
                lp += 1
            while rp < len(part2):
                new_arr.append(part2[rp])
                rp += 1 

            return new_arr
        
        return MergeSort(nums, 0, len(nums))
    



