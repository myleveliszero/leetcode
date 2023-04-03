# Status: Not Bad


class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()
        left, right = 0, len(people)-1
        boatcnt = 0
        while (left <= right):
            cursum = people[right]+people[left]
            if cursum <= limit:
                boatcnt += 1
                left += 1
                right -= 1
            else:
                boatcnt += 1
                right -= 1
        return boatcnt

solve = Solution()
print(solve.numRescueBoats([3,2,3,2,2], 6))
print(solve.numRescueBoats([1,2], 3))
print(solve.numRescueBoats([3,5,3,4], 5))