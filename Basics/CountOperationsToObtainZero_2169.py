# Status: Good


class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        i = 0
        while( num1 != 0 and num2 != 0):
            if num1 >= num2:
                num1 -= num2
            else:
                num2 -= num1
            i += 1
        return i

solve = Solution()
print(solve.countOperations(num1 = 2, num2 = 3))
print(solve.countOperations(num1 = 10, num2 = 10))