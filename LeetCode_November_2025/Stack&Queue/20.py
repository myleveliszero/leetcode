class Solution:    
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if stack:
                if stack[-1] == "(" and s[i] == ")":
                    stack.pop(); continue
                elif stack[-1] == "{" and s[i] == "}":
                    stack.pop(); continue
                elif stack[-1] == "[" and s[i] == "]":
                    stack.pop(); continue
            stack.append(s[i])

        return not stack
    
sol = Solution().isValid
# print(sol(")))()"))
print(sol("(())]()[]"))
print(sol("()[]{}"))