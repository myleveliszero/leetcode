from typing import List

class TreeNode:
    def __init__(self):
        self.parent = self
        self.height = 0

class UnionFind:
    def __init__(self, n):
        self.nodes = dict()
        for i in range(1, n+1):
            self.nodes[i] = TreeNode()
    
    def find(self, key):
        node = self.nodes[key]
        while node.parent != node:
            node = node.parent
        
        return node

    def union(self, edge):
        a, b = edge
        p1, p2 = self.find(a), self.find(b)
        if p1 == p2: # has cycle 
            return True
        
        if p1.height > p2.height:
            p2.parent = p1
        elif p1.height < p2.height:
            p1.parent = p2
        else:
            p2.parent = p1
            p1.height += 1
    
        return False  


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges))
        for edge in edges:
            val = uf.union(edge)
            if val:
                return edge


sol = Solution().findRedundantConnection
print(sol([[1,2],[2,3],[3,4],[1,4],[1,5]]))
print(sol([[1,2],[1,3],[2,3]]))

# [[1,2],[3,4],[5,6],[1,5],[7,8],[2,4],[5,8],[3,6]]

# import random as r

# def test(func1):
#     n = r.randrange(5,10)
#     edges = dict()
#     while len(edges) < n:
#         a, b = r.randrange(1, n+1), r.randrange(1, n+1)
#         if (a,b) not in edges and a < b:
#             edges[(a,b)] = None
    
#     edges = [list(edge) for edge in edges.keys()]
#     res = func1(edges)
#     print(edges)
#     # print(res)

# for _ in range(10):
#     test(sol)