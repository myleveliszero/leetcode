# Status: Good

class Solution:
    def calPoints(self, operations: list[str]) -> int:
        ans = []
        for i in range(len(operations)):
            if operations[i] == 'C':
                ans.pop()
            elif operations[i] == '+':
                ans.append(ans[-1]+ans[-2])
            elif operations[i] == 'D':
                ans.append(2*ans[-1])
            else:
                ans.append(int(operations[i]))
        return sum(ans)

solve = Solution()
print(solve.calPoints(operations = ["5","2","C","D","+"]))
print(solve.calPoints(operations = ["1","C"]))
print(solve.calPoints(operations = ["5","-2","4","C","D","9","+","+"]))