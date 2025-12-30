from typing import List

class TreeNode:
    def __init__(self, name, email):
        self.parent = self
        self.name = name
        self.mail = email
        self.height = 0

class UnionFind:
    def __init__(self, accounts):
        self.nodes = dict()
        for acc in accounts:
            name = acc[0]
            for i in range(1, len(acc)):
                if acc[i] not in self.nodes:
                    self.nodes[acc[i]] = TreeNode(name, acc[i])
        

    def find(self, key):
        node = self.nodes[key]
        while node.parent != node:
            node = node.parent
        parent = node.parent
        node = self.nodes[key]
        while node.parent != node:
            tmp = node.parent
            node.parent = parent
            node = tmp
        
        return node
        

    def union(self, edge):
        a, b = edge
        p1, p2 = self.find(a), self.find(b)
        if p1 == p2:
            return None
        
        if p1.height > p2.height:
            p2.parent = p1
        elif p1.height < p2.height:
            p1.parent = p2
        else:
            p2.parent = p1
            p1.height += 1
        
        return None

from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(accounts)
        for acc in accounts:
            for i in range(2, len(acc)):
                uf.union((acc[i-1], acc[i]))

        cluster = defaultdict(list)
        for key in uf.nodes.keys():
            parent = uf.find(key).mail
            cluster[parent].append(key)
        
        res = []
        for key in cluster.keys():
            name = [uf.nodes[key].name]
            res.append(name + sorted(cluster[key]))
            
        return res

sol = Solution().accountsMerge
# print(sol([["David","David0@m.co","David5@m.co","David0@m.co"],
#            ["Lily","Lily4@m.co","Lily2@m.co","Lily0@m.co"],
#            ["Fern","Fern5@m.co","Fern2@m.co","Fern6@m.co"],
#            ["Gabe","Gabe0@m.co","Gabe6@m.co","Gabe8@m.co"],
#            ["Alex","Alex7@m.co","Alex5@m.co","Alex7@m.co"],
#            ["Lily","Lily4@m.co","Lily6@m.co","Lily7@m.co"],
#            ["Alex","Alex0@m.co","Alex4@m.co","Alex5@m.co"],
#            ["John","John4@m.co","John2@m.co","John0@m.co"]]))

# print(sol([["David","David0@m.co","David1@m.co"],
#            ["David","David3@m.co","David4@m.co"],
#            ["David","David4@m.co","David5@m.co"],
#            ["David","David2@m.co","David3@m.co"],
#            ["David","David1@m.co","David2@m.co"]]))

print(sol(accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],
                      ["John","johnsmith@mail.com","john00@mail.com"],
                      ["Mary","mary@mail.com"],
                      ["John","johnnybravo@mail.com"]]))



[["John","John0@m.co","John2@m.co","John4@m.co"],
 ["Alex","Alex0@m.co","Alex4@m.co"],
 ["Lily","Lily6@m.co","Lily7@m.co"],
 ["Alex","Alex5@m.co","Alex7@m.co"],
 ["Gabe","Gabe0@m.co","Gabe6@m.co","Gabe8@m.co"],
 ["Fern","Fern2@m.co","Fern5@m.co","Fern6@m.co"],
 ["Lily","Lily0@m.co","Lily2@m.co","Lily4@m.co"],
 ["David","David0@m.co","David5@m.co"]]

[["David","David0@m.co","David5@m.co"],
 ["Fern","Fern2@m.co","Fern5@m.co","Fern6@m.co"],
 ["Gabe","Gabe0@m.co","Gabe6@m.co","Gabe8@m.co"],
 ["Alex","Alex0@m.co","Alex4@m.co","Alex5@m.co","Alex7@m.co"],
 ["Lily","Lily0@m.co","Lily2@m.co","Lily4@m.co","Lily6@m.co","Lily7@m.co"],
 ["John","John0@m.co","John2@m.co","John4@m.co"]]