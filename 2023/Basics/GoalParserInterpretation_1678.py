# Status: Good

class Solution:
    def interpret(self, command: str) -> str:
        nlen = len(command)
        s = ""
        i = 0
        while nlen > i:
            if command[i] == 'G':
                s += 'G'
                i += 1
            elif command[i] == '(' and command[i+1] == ")":
                s += 'o'
                i +=2
            else:
                s += "al"
                i += 4
        return s
    def version2(self, command):
        return command.replace('()', 'o').replace("(al)", "al")
    def version3(self, command):
        return command.replace('()', 'o').replace('(', "").replace(')', "")

solve = Solution()
print(solve.interpret("G()()()()(al)"))
print(solve.version2("G()()()()(al)"))
print(solve.version3("G()()()()(al)"))