from typing import List
import heapq as hq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        func = lambda x: (x[0]**2 + x[1]**2)**0.5
        
        for idx, val in enumerate(points):
            points[idx] = (func(val)*(-1), val)

        hq.heapify(points)
        for _ in range(len(points)-k):
            hq.heappop(points)

        for idx, val in enumerate(points):
            points[idx] = val[1]
        
        return points

        
    
sol = Solution().kClosest
print(sol(points = [[1,3],[-2,2]], k = 1))
