# Status: Good

class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        maxcandie = max(candies) - extraCandies
        return [maxcandie <= candie for candie in candies]

solve = Solution()
print(solve.kidsWithCandies(candies = [2,3,5,1,3], extraCandies = 3))