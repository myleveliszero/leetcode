# Status: Good

class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        answ = [0]*2*n
        for i in range(n):
            answ[2*i] = nums[i]
            answ[2*i+1] = nums[n+i]
        return answ
    def version2(self, nums, n):
        answ = []
        for i in range(n):
            answ.extend((nums[i],nums[n+i]))
        return answ
    # bitwise or, bitwise and, << , >> 
    def version3(self, nums, n):
        i,j = n-1, (2*n)-1
        while i != -1:
            nums[j] = nums[j] << 10
            nums[j] |= nums[i]
            i -= 1
            j -= 1
        i, j= 0, n
        while i < 2*n:
            num1 = nums[j] & 1023 
            num2 = nums[j] >> 10
            nums[i] = num1 
            nums[i+1] = num2
            i += 2
            j += 1
        return nums       

solve = Solution()
print(solve.shuffle([2,5,1,3,4,9,4,7], 4))
print(solve.version2([2,5,1,3,4,9,4,7], 4))
print(solve.version3([2,5,1,3,4,9,4,7], 4))

            
