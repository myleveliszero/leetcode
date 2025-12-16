# Status: Not bad

class Solution:
    def countGoodTriplets(self, arr: list[int], a: int, b: int, c: int) -> int:
        """
        A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:
        0 <= i < j < k < arr.length
        |arr[i] - arr[j]| <= a
        |arr[j] - arr[k]| <= b
        |arr[i] - arr[k]| <= c
        """
        # Naive approach
        answ = 0 
        alen = len(arr)
        for i in range(alen):
            for j in range(i+1, alen):
                firstcondition = abs(arr[i]-arr[j]) <= a
                if firstcondition:
                    for k in range(j+1, alen):
                        if abs(arr[j]-arr[k]) <= b and abs(arr[i]-arr[k]) <= c:
                            answ += 1
        return answ

solve = Solution()
print(solve.countGoodTriplets(arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3))
