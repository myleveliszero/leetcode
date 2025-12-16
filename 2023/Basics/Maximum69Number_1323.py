# Status: Good

class Solution:
    def maximum69Number (self, num: int) -> int:
        return str(num).replace('6', '9', 1)

solve = Solution()
print(solve.maximum69Number(9999))
print(solve.maximum69Number(96699))