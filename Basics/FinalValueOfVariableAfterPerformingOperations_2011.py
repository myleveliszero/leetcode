# Status: Good 

class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        answ = 0
        for i in operations:
            if i[1] == '+':
                answ += 1
            else:
                answ -= 1
        return answ
    
    def version2(self, op):
        return sum([1 if i[1] =='+' else -1 for i in op])

solve = Solution()
print(solve.finalValueAfterOperations(["--X","X++","X++"]))
print(solve.version2(["X++","X++","--X","X--","++X"]))
