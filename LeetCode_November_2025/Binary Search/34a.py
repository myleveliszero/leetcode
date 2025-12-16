def searchRange(nums, target: int):
    def bs(arr, tar):
        left, right = 0, len(arr)-1
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] < tar:
                left = mid+1
            else:
                right = mid-1
        return left
    
    l, r = bs(nums,target-0.9), bs(nums, target+0.9)
    
    if l == r:  
        return [-1,-1]
    else: 
        return [l, r-1]
    

print(searchRange([5,7,7,8,8,10,11,11,11,22], 11))

print(searchRange([5,7,7,8,8,10], 8))
print(searchRange([5,7,7,8,8,8,8,8,9,10,11], 8))
print(searchRange([5,7,7,8,8,10], 6))

print(searchRange([], 0))

print(searchRange([5,7,7], 128))

print(searchRange([5,7,7,8,8,10,11,11,11,22], 5))