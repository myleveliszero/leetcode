from typing import List
import heapq as hq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for idx, val in enumerate(stones):
            stones[idx] = -val 
        hq.heapify(stones)
        while len(stones) > 1:
            val1, val2 = hq.heappop(stones) , hq.heappop(stones)
            if val1 != val2:
                hq.heappush(stones, val1-val2)
        
        if stones:  
            return stones[0]*(-1)
        return 0


sol = Solution().lastStoneWeight

print(sol(stones = [2,7,4,1,8,1]))