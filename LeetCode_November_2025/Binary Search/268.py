#2147483647


def missingNumber(nums) -> int:
    nums.sort()
    l, r = 0, len(nums)-1
    while l <= r:
        m = (r-l)//2 + l
        if m == nums[m]:
            l = m+1
        elif m < nums[m]:
            r = m-1
    return l



# print(missingNumber([0,1]))
# print(missingNumber([0,2]))
print(missingNumber([0]))
print(missingNumber([9,6,4,2,3,5,7,0,1]))
print(missingNumber([9,6,4,2,3,1,7,0,8]))