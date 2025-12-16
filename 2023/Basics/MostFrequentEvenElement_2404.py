# Status: Bad

class Solution:
    def mostFrequentEven(self, nums: list[int]) -> int:
        temp = set(nums)
        check = [i for i in temp if i%2 == 0 ]
        check.sort()
        if check == []:
            return -1
        most = []
        for i in check:
            cnt = 0
            for j in nums:
                if j == i:
                    cnt += 1
            most.append(cnt)
        idx = 0 
        val = 0
        for i in range(len(most)):
            if most[i] > val:
                val = most[i]
                idx = i
            
        return check[idx]

solve = Solution()
print(solve.mostFrequentEven(nums = [0,1,2,2,4,4,1]))