# Status: Bad

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        pass
    def simple(self, c):
        RANGE = 46341
        if c < RANGE:
            RANGE = c+1 
        left, right = 0, RANGE-1
        while (left <= right):
            ishypotenuse = left**2 + right**2
            if ishypotenuse == c:
                return True
            elif ishypotenuse > c:
                right -= 1
            else:
                left += 1

        return False

solve = Solution()
print(solve.simple(5))
print(solve.simple(25))
print(solve.simple(165))