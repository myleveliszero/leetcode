# Status: Not Bad

class Solution:
    def checkDistances(self, s: str, distance: list[int]) -> bool:
        visited = []
        for i in range(len(s)):
            if s[i] not in visited:
                for j in range(i+1, len(s)):
                    if s[i] == s[j]:
                        if j-i-1 == distance[ord(s[i])-97]:
                            visited.append(s[i])    
                            break
                        else:
                            return False
        return True

solve = Solution()
print(solve.checkDistances(s = "abaccb", 
distance = [1,3,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]))
    