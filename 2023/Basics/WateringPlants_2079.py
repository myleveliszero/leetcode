# Status: Good

class Solution:
    def wateringPlants(self, plants: list[int], capacity: int) -> int:
        answ, plen = 0, len(plants)
        curcan = capacity
        for i in range(plen):
            answ += 1
            if curcan < plants[i]:
                answ += i*2
                curcan = capacity
            curcan -= plants[i]  
        return answ

solve = Solution()
print(solve.wateringPlants(plants = [2,2,3,3], capacity = 5))
print(solve.wateringPlants(plants = [1,1,1,4,2,3], capacity = 4))
print(solve.wateringPlants(plants = [7,7,7,7,7,7,7], capacity = 8))
