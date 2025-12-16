# Status: Good

import time
class Solution:
    # Basic Binary Search
    def mySqrt(self, x: int) -> int:
        if x == 0: 
            return 0
        RANGE = 46341
        left, right = 0, RANGE-1
        while left <= right:
            mid = (left + right)//2
            if mid*mid == x:
                return mid
            elif mid*mid < x:
                if (mid+1)*(mid+1) > x:
                    return mid
                else:
                    left = mid+1
            elif mid*mid > x:
                if (mid-1)*(mid-1) < x:
                    return mid-1
                else:
                    right = mid-1
begin = time.time()
solve = Solution()
print(solve.mySqrt(4))
print(solve.mySqrt(15))
print(solve.mySqrt(153))
print(solve.mySqrt(2147483647))
print(solve.mySqrt(134))
end = time.time()
print(f"Execution time: {(end-begin)*1000}")