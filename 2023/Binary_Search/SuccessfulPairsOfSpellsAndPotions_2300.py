# Status: Not Bad

class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        potions.sort()
        ans = []
        for i in spells:
            l,r = 0, len(potions)-1
            while l <= r:
                m = l + (r-l)//2
                if i*potions[m] >= success:
                    r = m-1
                else:
                    l = m+1
            ans.append(len(potions)-l)
        return ans