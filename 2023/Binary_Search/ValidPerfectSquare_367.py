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
            else:               # elif isperfect >= num:    
                right = mid-1
        return False
    def isPSqrtVersion2(self, num: int) -> bool:
        left, right = 0, num
        while left <= right:
            mid = left + (right - left)//2
            isperfect = mid*mid
            if isperfect == num:
                return True
            elif isperfect < num:
                left = mid+1
            else:               # elif isperfect >= num:
                right = mid-1
        return False
    def Newton(self, num):
        x = num
        while (x*x > num):
            x = (x+num/x)//2
        return x*x == num
    def oddsequence(self, num):
        # 1 + 3 + 5 + 7
        #   4   9   16
        i = 1
        while (num > 0):
            num -= i
            i += 2
        return num == 0

solve = Solution()
print(solve.isPerfectSquare(4), end = " --> ")
print(solve.isPerfectSquare(15), end = " --> ")
print(solve.isPerfectSquare(153), end = " --> ")
print(solve.isPerfectSquare(169), end = " --> ")
print(solve.isPerfectSquare(2147483647), end = " --> ")
print(solve.isPerfectSquare(1073741824))

print(solve.Newton(153), end = " --> ")
print(solve.Newton(169))

print(solve.isPSqrtVersion2(153), end = " --> ")
print(solve.isPSqrtVersion2(169), end = " --> ")
print(solve.isPSqrtVersion2(2147483647), end = " --> ")
print(solve.isPSqrtVersion2(1073741824))

print(solve.oddsequence(153), end = " --> ")
print(solve.oddsequence(169))