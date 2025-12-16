from typing import*
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = dict()
        for i in range(len(nums)):
            if nums[i] in hmap:
                hmap[nums[i]] += 1
            else:
                hmap[nums[i]] = 1
        
        temp = sorted(hmap.items(), key=lambda item: item[1], reverse=True)
        res = []
        for i in range(k):
            res.append(temp[i][0])
        
        return res
    
sol = Solution().topKFrequent
print(sol([1,2,1,2,1,2,3,1,3,2], 2))