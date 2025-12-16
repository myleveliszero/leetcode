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
        for char in s:
            pair += char == '|'
            answ += char == '*' and pair % 2 == 0
        return answ
    def version3(self, s):
        return sum(word.count('*') for word in s.split('|')[0::2])


solve = Solution()
print(solve.countAsterisks( s = "l|*e*et|c**o|*de|"))
print(solve.version2( s = "l|*e*et|c**o|*de|"))
print(solve.version3( s = "l|*e*et|c**o|*de|"))