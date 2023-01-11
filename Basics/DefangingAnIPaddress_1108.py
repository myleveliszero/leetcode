# Status: Good

class Solution:
    def defangIPaddr(self, address: str) -> str:
        answ = []
        for i in address:
            if i == '.':
                answ.append("[.]")
            else:
                answ.append(i)
        return "".join(answ)
    
    def version2(self, address):
        answ = ""
        for i in address:
            if i == '.':
                answ += "[.]"
            else:
                answ += i
        return answ

    def version3(self, address):
        return address.replace('.', "[.]")
    
    def version4(self, address):
        return "[.]".join(address.split('.'))
    
    def version5(self, address):
        return "".join([ch if ch!='.' else "[.]" for ch in address])

solve = Solution()
print(solve.defangIPaddr("255.100.50.0"))
print(solve.version2("255.100.50.0"))
print(solve.version3("255.100.50.0"))
print(solve.version4("255.100.50.0"))
print(solve.version5("255.100.50.0"))
