def findPeakElement(nums) -> int:
    if len(nums) == 1:
        return 0
    
    left, right = 0, len(nums)-1
    while left <= right:
        mid = (right-left)//2 + left
        if nums[mid] > nums[mid-1] and mid==right:
            return mid
        elif nums[mid] > nums[mid+1] and mid==left:
            return mid
        elif nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
            return mid
        elif nums[mid] < nums[mid+1]:
            left = mid+1
        elif nums[mid] > nums[mid+1]:
            right = mid-1
        
print(findPeakElement([123415])) 
print(findPeakElement([5234,-13251]))
print(findPeakElement([-12341,13255]))

print(findPeakElement([1,2,1,3,5,6,4]))
print(findPeakElement([1,2,1,3,7,6,5]))
print(findPeakElement([9,7,4,3,2,6,4]))
print(findPeakElement([1,7,4,3,2,6,4]))
print(findPeakElement([1,2,4,3,5,6,4]))
print(findPeakElement([1,2,3,1]))
print(findPeakElement([11,13,15,17]))
print(findPeakElement([4,5,6,7,8,9,10,11,12,0,1,2]))