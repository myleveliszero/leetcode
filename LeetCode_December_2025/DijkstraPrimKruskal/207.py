from typing import List
class Solution:
    def dfs(self, adj, src, visit, path):
        if src in path:
            return True
        if src in visit:
            return False
        
        visit.add(src)
        path.add(src)
        for nieghbour in adj[src]:
            if self.dfs(adj, nieghbour, visit, path):
                return True            
        path.remove(src)
        return False

        

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {key:[] for key in range(numCourses)}
        for edge in prerequisites:
            destination, source = edge
            adj[source].append(destination)
        
        visit = set()
        for src in range(numCourses):
            if self.dfs(adj, src, visit, path=set()):
                return False
        
        return True




sol = Solution().canFinish
print(sol(numCourses = 3, prerequisites = [[0,2],[1,2],[2,0]]))
# print(sol(numCourses = 2, prerequisites = [[1,0]]))
# print(sol(numCourses = 2, prerequisites = [[1,0],[0,1]]))
