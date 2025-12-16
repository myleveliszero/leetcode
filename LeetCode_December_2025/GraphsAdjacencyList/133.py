from typing import Optional
from collections import deque

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        def bfs(node, visit, edges):
            q = deque()
            edges = set()
            visit = set()
            q.append(node)
            while q:
                cur_node = q.popleft()
                if cur_node.val in visit:
                    continue
                visit.add(cur_node.val)
                for n in cur_node.neighbors:
                    edges.add((cur_node.val, n.val))
                    q.append(n)
            return (visit, edges)
        
        if node is None:
            return node 
      
        visit, edges = bfs(node, set(), set())
        adj_lst = dict()
        for v in visit:
            adj_lst[v] = Node(v)
        
        for src, dst in edges:
            adj_lst[src].neighbors.append(adj_lst[dst])

        return adj_lst[1]
 
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
a.neighbors = [b,d]
b.neighbors = [a,c]
c.neighbors = [b,d]
d.neighbors = [a,c]

sol = Solution().cloneGraph

res = sol(a)
a.val = 99
if res:
    print(res.neighbors)
    print(res.val)