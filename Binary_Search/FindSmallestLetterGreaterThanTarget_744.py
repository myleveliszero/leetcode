# Status: Good

class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        ans = letters[0]
        left, right = 0, len(letters)-1
        while left <= right:
            mid = left + (right - left)//2
            if letters[mid] > target:
                ans = letters[mid]
                right = mid-1
            else:
                left = mid+1
        return ans
    def version2(self, letters, target):
        if target >= letters[-1] or target < letters[0]:
            return letters[0]

        left, right = 0, len(letters)-1
        while left <= right:
            mid = left + (right - left)//2
            if letters[mid] > target:
                right = mid-1
            else:
                left = mid+1
        return letters[left]


solve = Solution()
print(solve.nextGreatestLetter(letters = ["c","f","j"], target = "a"))
print(solve.nextGreatestLetter(letters = ["c","f","j"], target = "c")) 
print(solve.nextGreatestLetter(letters = ["x","x","y","y"], target = "z"))
print(solve.nextGreatestLetter(letters = ["a","x","x","x","x","x","y","y","y","y"], target = "b"))
print('---------------------------------------')
print(solve.version2(letters = ["c","f","j"], target = "j"))
print(solve.version2(letters = ["c","f","j"], target = "c")) 
print(solve.version2(letters = ["x","x","y","y"], target = "z"))
print(solve.version2(letters = ["a","x","x","x","x","x","y","y","y","y"], target = "b"))
