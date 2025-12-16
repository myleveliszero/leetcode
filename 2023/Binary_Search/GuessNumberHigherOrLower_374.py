# Status: Good

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
PICK = 6 # 1 <= pick <= n
def guess(num: int) -> int:
    if num > PICK:
        return -1
    elif num < PICK:
        return 1
    else:
        return 0
class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n # range(1,n),  1 <= n <= 2^31-1
        while left <= right:
            mid = left + (right-left)//2
            res = guess(mid)
            if res == -1:
                right = mid - 1
            elif res == 1:
                left = mid +1
            else:
                return mid
        return -1

solve = Solution()
print(solve.guessNumber(10))