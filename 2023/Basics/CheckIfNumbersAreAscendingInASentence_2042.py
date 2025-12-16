# Status: Not Bad

class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        nums = ""
        for i in s:
            if i == " ":
                nums += i    
            elif i in "1234567890":
                nums += i
        nums = nums.split()
        nums = [int(x) for x in nums]
        print(nums)
        for i in range(len(nums)-1):
            if nums[i+1] <= nums[i]:
                return False 

        return True
    
solve = Solution()
print(solve.areNumbersAscending(s = "1 box has 3 blue 4 red 6 green and 12 yellow marbles"))

print(solve.areNumbersAscending(s = "hello world 5 x 5"))

print(solve.areNumbersAscending(s = "sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s"))