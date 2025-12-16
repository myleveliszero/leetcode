# Status: Good

class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        prev = 0
        for i in range(len(gain)):
            gain[i] += prev
            prev = gain[i]
        gain.append(0)
        return max(gain)
    def version2(self, gain):
        cur = 0
        answmax = 0 
        for g in gain:
            cur += g
            if answmax < cur:
                answmax = cur
        return answmax
solve = Solution()
print(solve.largestAltitude(gain = [-5,1,5,0,-7]))