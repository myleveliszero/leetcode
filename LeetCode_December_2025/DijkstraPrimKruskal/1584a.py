from typing import List 

# Kruskal's algorithm
class TreeNode:
    def __init__(self):
        self.parent = self
        self.height = 0

class UnionFind:
    def __init__(self, nodes):
        self.root = dict()
        for node in nodes:
            self.root[tuple(node)] = TreeNode()

    def find(self, val)-> TreeNode:
        node = self.root[val]
        while node != node.parent:
            tmp = node.parent
            node.parent = node.parent.parent
            node = tmp 
        
        return node

    def union(self, a, b)-> None:
        n1, n2 = self.find(a), self.find(b)
        if n1 == n2:
            return False
        
        if n1.height > n2.height:
            n2.parent = n1
        elif n2.height >  n1.height:
            n1.parent = n2
        else:
            n2.parent = n1 
            n1.height += 1

        return True
        
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        uf = UnionFind(points)
        manh = lambda p1,p2: abs(p1[0]-p2[0])+abs(p1[1]-p2[1])
        edges = []
        for p1 in range(len(points)):
            for p2 in range(len(points)):
                if p1 != p2:
                    edges.append((manh(points[p1],points[p2]), points[p1], points[p2]))
        
        total_cost = 0
        edges.sort(key=lambda x: x[0])
        count = 0
        for edge in edges:
            cost, p1, p2 = edge
            if uf.union(tuple(p1), tuple(p2)):
                total_cost += cost
                count += 1 
                if count == len(points): break
        
        return total_cost
        


sol = Solution().minCostConnectPoints
print(sol([[0,0],[2,2],[3,10],[5,2],[7,0]]))
print(sol([[3,12],[-2,5],[-4,1]]))

# prim = __import__('1584')
# sol2 = prim.Solution().minCostConnectPoints

# import random as r
# def test(f1, f2):
#     # n = r.randrange(100, 200)
#     n = 1000
#     points = []
#     vis = set()
#     for _ in range(n):
#         point = [r.randrange(-50,50), r.randrange(-50,50)]
#         if tuple(point) not in vis:
#             points.append(point)
#             vis.add(tuple(point))
        
#     res1 = f1(points)
#     res2 = f2(points)
#     print(points)
#     if res1 != res2:
#         print(points)
#         print("-------------")

# test(sol, sol2)
# for i in range(100):
#     test(sol, sol2)
