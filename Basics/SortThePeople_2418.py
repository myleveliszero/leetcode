# Status: Good

class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        sortpeople = []
        nlen = len(names)
        for i in range(nlen):
            sortpeople.append((heights[i], names[i]))
        sortpeople.sort(reverse=True)
        answ = []
        for i in range(nlen):
            answ.append(sortpeople[i][1])
        return answ
    def version2(self, names, heights):
        return [name for height, name in sorted(zip(heights,names), reverse=True)]


solve = Solution()
print(solve.sortPeople(names = ["Mary","John","Emma"], heights = [180,165,170]))
print(solve.version2(names = ["Alice","Bob","Bob"], heights = [155,185,150]))
print(solve.version2(names = ["Mary","John","Emma"], heights = [180,165,170]))