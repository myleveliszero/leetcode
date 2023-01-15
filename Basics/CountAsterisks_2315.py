# Status: Good 

class Solution:
    def countAsterisks(self, s: str) -> int:
        answ = 0
        condition = 0
        allasterisks = 0
        for char in s:
            if '|' == char:
                if condition:
                    condition = 0
                else:
                    condition = 1
            if '*' == char:
                if condition:
                    answ += 1
                allasterisks += 1
            
        return allasterisks - answ
    def version2(self, s):
        answ, pair = 0, 0
        for i in s:
            if i == "|":
                pair += 1
            elif pair % 2 == 0 and i == "*":
                answ += 1
        return answ

solve = Solution()
print(solve.countAsterisks( s = "l|*e*et|c**o|*de|"))
