# Status: Good

class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        from_ = set(f for f,t in paths)
        to_ = set(t for f,t in paths)
        return list(to_- from_)[0]

solve = Solution()
print(solve.destCity(paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))
print(solve.destCity(paths = [["B","C"],["D","B"],["C","A"]]))
print(solve.destCity(paths = [["A","Z"]]))