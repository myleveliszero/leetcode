from typing import*
from collections import deque
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = deque(students)
        sandwiches.reverse()
        length = len(students)
        while students:
            for _ in range(len(students)):
                stud = students.popleft()
                if  stud == sandwiches[-1]:
                    sandwiches.pop()
                else:
                    students.append(stud)
            if length == len(students):
                return len(students)
            length = len(students)
        return 0
    
sol = Solution().countStudents
# print(sol(students = [1,1,0,0], sandwiches = [0,1,0,1]))
print(sol(students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]))
print(sol(students = [1,1,0,0], sandwiches = [0,1,0,1]))
