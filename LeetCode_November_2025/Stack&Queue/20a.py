class Solution:
    def isValidPair(self, prev, cur):
        if  prev == "(" and cur == ")" or \
            prev == "{" and cur == "}" or \
            prev == "[" and cur == "]":
            return True
        return False
    
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if stack:
                if self.isValidPair(stack[-1], s[i]):
                    stack.pop()
                    continue
            stack.append(s[i])

        return not stack
    
sol = Solution().isValid
# print(sol(")))()"))
print(sol("(())]()[]"))
print(sol("()[]{}"))