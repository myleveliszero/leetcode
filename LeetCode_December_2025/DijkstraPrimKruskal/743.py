from typing import List
import heapq as hq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {key:[] for key in range(1, n+1)}
        # u - sourse, v - target, w - cost
        for u, v, w in times: 
            adj[u].append((w,v))

        short = {key: None for key in range(1, n+1)}
        min_q = []
        for edg in adj[k]:
            hq.heappush(min_q, edg)
        
        short[k] = 0
        visit = set()
        visit.add(k)
        while min_q:
            cost, u = hq.heappop(min_q)
            if u in visit:
                continue
            visit.add(u)
            if short[u] is None:
                short[u] = cost
            for w, v in adj[u]:
                if u != v:
                    hq.heappush(min_q, (cost+w, v))

        max_val = 0
        for val in short.values():
            if val is None:
                return -1
            max_val = max_val if max_val > val else val

        return max_val
        

sol = Solution().networkDelayTime
print(sol([[1,2,1],[2,3,7],[1,3,4],[2,1,2]], n = 4, k = 1))     
print(sol([[1,2,1],[2,1,3]], n = 2, k = 2))     
print(sol(times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 1))     
print(sol(times = [[1,2,1]], n = 2, k = 1))     