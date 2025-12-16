# Status: Good

class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s = s[::-1]
        print(s)
    def version2(self, s):
        s.reverse()
        print(s)
    def version3(self, s):
        for i in range(len(s)//2):
            temp = s[i]
            s[i] = s[~i]
            s[~i] = temp
        print(s)

solve = Solution()
solve.reverseString(s = ["h","e","l","l","o"])
solve.reverseString(s = ["H","a","n","n","a","h"])
solve.version2(s = ["h","e","l","l","o"])
solve.version3(s = ["H","a","n","n","a","h"])