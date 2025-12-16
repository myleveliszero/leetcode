from typing import List
import collections 
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = collections.Counter(students)
        n, k = len(students), 0
        while k < n and count[sandwiches[k]]:
            count[sandwiches[k]] -= 1
            k += 1
        return n-k


  
sol = Solution().countStudents
print(sol(students = [1,1,1,1], sandwiches = [0,0,0,0]))
print(sol(students = [1,1,1,1], sandwiches = [1,0,0,0]))
print(sol(students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]))
print(sol(students = [1,1,0,0], sandwiches = [0,1,0,1]))
