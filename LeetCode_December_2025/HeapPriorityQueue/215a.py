from typing import List
import heapq as hq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for idx, val in enumerate(nums):
            nums[idx] = -val
        hq.heapify(nums)
        iter = 1
        while iter < k:
            hq.heappop(nums)
            iter += 1

        return -hq.heappop(nums)
        
sol = Solution().findKthLargest
print(sol(nums = [3,2,3,1,2,4,5,5,6], k = 5
))