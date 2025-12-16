from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(adj_list, root, visit, seen):
            if root in visit:
                return True
            if root in seen:
                return
            
            visit.add(root)
            seen.add(root)
            for node in adj_list[root]:
                cycle = dfs(adj_list, node, visit, seen)
                if cycle:
                    return True
            visit.remove(root)
            return False 
        
        
        adj_list = dict()
        for dst, src in prerequisites:
            if src not in adj_list:
                adj_list[src] = set()
            if dst not in adj_list:
                adj_list[dst] = set()
            adj_list[src].add(dst)
            if src in adj_list[dst] and dst in adj_list[src]:
                return False
        
        seen = set()
        for node in adj_list.keys():
            if node not in seen:
                cycle = dfs(adj_list, node, set(), seen)
                if cycle:
                    return False
        
        return True


        
        



sol = Solution().canFinish


print(sol(numCourses=4, prerequisites=[[1,0],[2,1],[3,2],[1,3]])) # True
print(sol(numCourses=7, prerequisites=[[1,0],[0,3],[0,2],[3,2],[2,5],[4,5],[5,6],[2,4]])) # True
print(sol(numCourses=3, prerequisites=[[1,0],[0,2],[2,1]])) # False
print(sol(numCourses=5, prerequisites=[[1,0],[3,1],[3,2],[2,0],[1,3]])) # False becase [3,1],[1,3]
print(sol(numCourses=5, prerequisites=[[1,0],[3,1],[3,2],[2,0]])) # True
print(sol(numCourses=5, prerequisites=[[1,0],[3,1],[3,2],[4,3]])) # True
print(sol(numCourses=5, prerequisites=[[2,0],[4,1]])) # True

# False
# True
# False
# False
# True
# True
# True