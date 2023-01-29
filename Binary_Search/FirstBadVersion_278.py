# Status: Good

# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    if version >= 636:
        return True
    else:
        return False

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left , right = 1, n
        while left <= right:
            mid = left+(right-left)//2
            if isBadVersion(mid):
                right = mid-1
            else:
                left = mid+1
        return left
            

solve = Solution()
# bad = 4
# print(solve.firstBadVersion(n = 8))
# bad = 636
print(solve.firstBadVersion(n = 15153))