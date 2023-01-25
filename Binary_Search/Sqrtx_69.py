# Status: Not Bad

class Solution:
    # Basic Binary Search
    def mySqrt(self, x: int) -> int:
        if x == 0: 
            return 0
        RANGE = 46341
        nums = [i for i in range(1, RANGE)]
        left, right = 0, RANGE-1
        while left <= right:
            mid = (left + right)//2
            i = nums[mid]
            if i*i == x:
                return i
            elif i*i < x:
                if (i+1)*(i+1) > x:
                    return i
                else:
                    left = i+1
            elif i*i > x:
                if (i-1)*(i-1) < x:
                    return i-1
                else:
                    right = i-1

solve = Solution()
print(solve.mySqrt(4))
print(solve.mySqrt(15))
print(solve.mySqrt(153))
print(solve.mySqrt(56))
print(solve.mySqrt(134))
