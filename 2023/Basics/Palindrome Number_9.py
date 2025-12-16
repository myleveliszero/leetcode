# Status: Good

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x)[::-1] == str(x)
    def version2(self, x):
        if x < 0:
            return False

        x = str(x)
        for i in range(len(x)//2):
            if x[i] != x[~i]:
                return False
        return True
    
solve = Solution()
print(solve.isPalindrome(121))
print(solve.version2(121))