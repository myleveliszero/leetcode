class Solution:
    def sortEvenOdd(self, nums: list[int]) -> list[int]:
        odd, even = [], []
        for i in range(len(nums)):
            if i%2 == 0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        even.sort()
        odd.sort(reverse=True)
        ans = []
        if len(nums)%2 == 0:
            for i in range(len(nums)//2):
                ans.append(even[i])
                ans.append(odd[i])
        else:
            for i in range((len(nums)-1)// 2):
                ans.append(even[i])
                ans.append(odd[i])
            ans.append(even[-1])

        return ans 

solve = Solution()
print(solve.sortEvenOdd([4,1,2,3]))

print(solve.sortEvenOdd([4,1,2,3,5,11,17]))

print(solve.sortEvenOdd([4,1,2,3,32]))