class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: -x[1])
        ans = 0
        for numbox, units in boxTypes:
            if truckSize > numbox:
                truckSize -= numbox
                ans += numbox * units
            else:
                ans += truckSize * units
                return ans
        return ans

solve = Solution()
print(solve.maximumUnits(boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10))