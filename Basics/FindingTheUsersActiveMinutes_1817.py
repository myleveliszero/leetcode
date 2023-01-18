# Status: Good

from collections import defaultdict

class Solution:
    def findingUsersActiveMinutes(self, logs: list[list[int]], k: int) -> list[int]:
        uam = defaultdict(set)
        for user in logs:
            uam[user[0]].add(user[1])
        answ = [0]*(k)
        for j in uam:
            answ[len(uam[j]) - 1] += 1
        return answ

solve = Solution()
print(solve.findingUsersActiveMinutes(logs = [[0,5],[1,2],[0,2],[0,5],[1,3]], k = 5))
print(solve.findingUsersActiveMinutes(logs = [[1,1],[2,2],[2,3]], k = 4))
