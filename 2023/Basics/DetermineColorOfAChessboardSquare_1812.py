# Status: Good

class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        if coordinates[0] in "aceg":
            if int(coordinates[1]) % 2 == 0:
                return True
            else:
                return False
        else:
            if int(coordinates[1]) % 2 == 0:
                return False
            else:
                return True
    def version2(self, c):
        return (ord(c[0])+ord(c[1])) % 2 == 1


solve = Solution()
print(solve.squareIsWhite(coordinates="a1"))
print(solve.squareIsWhite(coordinates="c7"))
print(solve.squareIsWhite(coordinates="h3"))
print(solve.version2(c="a1"))
print(solve.version2(c="c7"))
print(solve.version2(c="h3"))