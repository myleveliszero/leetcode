from typing import List
import heapq as hq
# Prim's algorithm 
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visit = set()
        manh = lambda p1,p2: abs(p1[0]-p2[0])+abs(p1[1]-p2[1])
        min_q = []
        p1 = points[0]
        for p2 in range(1, len(points)):
            hq.heappush(min_q, [manh(p1,points[p2]), points[p2]])
            # hq.heappush(min_q, [manh(p1,points[p2]), p1, points[p2]])
        visit.add((p1[0], p1[1]))
        total_cost = 0
        while len(visit) != len(points):
            cost, p2 = hq.heappop(min_q)
            # min_q.clear()
            if (p2[0],p2[1]) in visit:
                continue
            total_cost += cost
            visit.add((p2[0], p2[1]))
            for p1 in points:
                if (p1[0],p1[1]) not in visit:
                    hq.heappush(min_q, [manh(p1,p2), p1])
        
        return total_cost
            

sol = Solution().minCostConnectPoints
print(sol([[0,0],[2,2],[3,10],[5,2],[7,0]]))
print(sol([[3,12],[-2,5],[-4,1]]))
