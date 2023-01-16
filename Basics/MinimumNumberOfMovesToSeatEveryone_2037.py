# Status: Good

class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        seats.sort()
        students.sort()
        print(seats)
        print(students)
        answ = 0
        for i in range(len(students)):
            answ += abs(students[i]-seats[i])
        return answ
    def version2(self, seats, students):
        import numpy as np
        return np.absolute(np.sort(np.asarray(seats))-np.sort(np.asarray(students))).sum()


solve = Solution()
print(solve.minMovesToSeat(seats = [3,1,5], students = [2,7,4]))
print(solve.version2(seats = [3,1,5], students = [2,7,4]))