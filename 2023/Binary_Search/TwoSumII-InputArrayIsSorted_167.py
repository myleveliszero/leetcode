# Status: Good

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        nlen = len(numbers)
        for i in range(nlen):
            low, high = i+1, nlen-1
            Y = target - numbers[i]
            while low <= high:
                mid = low + (high-low)//2
                # cursum = numbers[mid]+numbers[i]
                if  numbers[mid] == Y: #  cursum == target
                    return [i+1, mid+1] 
                elif numbers[mid] > Y:
                    high = mid-1
                else:
                    low = mid+1
        return [-1,-1]

    def twopointers(self, numbers, target):
        left, right = 0, len(numbers)-1
        while left < right:
            cursum = numbers[left]+numbers[right]
            if cursum == target:
                return [left+1 , right+1]
            elif cursum > target:
                right -= 1
            else:
                left += 1

    def dictionary_m(self, numbers, target):
        dicti = {}
        for idx, val in enumerate(numbers):
            if target - val in dicti:
                return [dicti[target-val]+1, idx+1]
            dicti[val] = idx 

    def bruteforce(self, numbers, target): # TLE
        nlen = len(numbers)
        for i in range(nlen):
            for j in range(i+1, nlen):
                if numbers[i]+numbers[j] == target:
                    return [i+1,j+1]
                elif numbers[i]+numbers[j] > target:
                    break

solve = Solution()
print(solve.twoSum(numbers =[2,3,4,6,8,10,12,13,14,22,20,26], target = 29))

print(solve.twopointers(numbers = [2,3,4,6,8,10,12,13,14,22,20,26], target = 29))

print(solve.dictionary_m(numbers = [2,3,4,6,8,10,12,13,14,22,20,26], target = 29))

print(solve.bruteforce(numbers = [2,3,4,6,8,10,12,13,14,22,20,26], target = 29))