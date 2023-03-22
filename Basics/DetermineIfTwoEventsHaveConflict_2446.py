# Status: Good

class Solution:
    def haveConflict(self, event1: list[str], event2: list[str]) -> bool:
        a,b = event1[0], event1[1]
        c,d = event2[0], event2[1]
        if (a <= c <= b or a <= d <= b or (c<=a and b <= d)):
            return True
        else:
            return False

solve = Solution()
print(solve.haveConflict(["15:19","17:56"], ["14:11","20:02"]))
print(solve.haveConflict(["16:53","19:00"], ["10:33","18:15"]))
print(solve.haveConflict(["15:19","17:56"], ["14:11","20:02"]))
print(solve.haveConflict(["10:00","11:00"], ["14:00","15:00"])) 
print(solve.haveConflict(["01:15","02:00"], ["02:00","03:00"])) 