# Status: Good

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        RANGE = 46341
        left, right = 0, RANGE-1
        while left <= right:
            mid = left + (right - left)//2
            isperfect = mid*mid
            if isperfect == num:
                return True
            elif isperfect < num:
                left = mid+1
            elif isperfect >= num:
                right = mid-1
        return False
    def version2(self, num: int) -> bool:
        left, right = 0, num
        while left <= right:
            mid = left + (right - left)//2
            isperfect = mid*mid
            if isperfect == num:
                return True
            elif isperfect < num:
                left = mid+1
            elif isperfect >= num:
                right = mid-1
        return False

    def Newton(self, num):
        x = num
        while (x*x > num):
            x = (x+num/x)//2
        return x*x == num

solve = Solution()
print(solve.isPerfectSquare(4))
print(solve.isPerfectSquare(15))
print(solve.isPerfectSquare(153))
print(solve.isPerfectSquare(169))
print(solve.isPerfectSquare(2147483647))
print(solve.isPerfectSquare(1073741824))
print(solve.Newton(153))
print(solve.Newton(169))
print(solve.version2(153))
print(solve.version2(169))
print(solve.version2(2147483647))
print(solve.version2(1073741824))