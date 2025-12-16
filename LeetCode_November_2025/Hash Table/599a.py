from typing import*
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        minsum = float('inf')
        h1 = {list1[i]:i for i in range(len(list1))}
        res, sum = [], None
        for i in range(len(list2)):
            if list2[i] in h1:
                sum = i + h1[list2[i]]
                if sum < minsum:
                    res.clear()
                    res.append(list2[i])
                    minsum = sum
                elif sum == minsum:
                    res.append(list2[i])
        return res
    
sol = Solution().findRestaurant
print(sol(list1 = ["Shogun","Tapioca Express","Burger King","KFC"], 
          list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]))
    
print(sol(list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger King"]))
print(sol(["S","TEXP","BK","KFC"], ["KFC","BK","S"]))

    

