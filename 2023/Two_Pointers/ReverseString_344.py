# Status: Good

class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        print(s)
        for i in range(len(s)//2):
            s[i], s[~i] = s[~i], s[i]

        print(s)
        
solve = Solution()
solve.reverseString(s = ["h","e","l","l","o"])
solve.reverseString(s = ["H","a","n","n","a","h"])