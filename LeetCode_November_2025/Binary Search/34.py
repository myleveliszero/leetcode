def searchRange(nums, target: int):
    l, r = 0, len(nums)-1 
    #searching first occurence of the target
    while l<=r:
        m = (r-l)//2 + l
        if nums[m] == target:
            # searching left part
            l1, r1 = l, m
            while l1 <= r1:
                m1 = (r1-l1)//2 + l1 
                if nums[m1] >= target:
                    r1 = m1-1
                elif nums[m1] < target:
                    l1 = m1+1
            # searching right part
            l2, r2 = m, r
            while l2 <= r2:
                m2 = (r2-l2)//2 + l2
                if nums[m2] <= target: 
                    l2 = m2+1
                elif nums[m2] > target:
                    r2 = m2-1
            # found most left index and most right index
            return l1, r2
        elif nums[m] < target:
            l = m+1
        elif nums[m] > target:
            r = m-1

    return [-1,-1]

print(searchRange([5,7,7,8,8,10,11,11,11,22], 11))

print(searchRange([5,7,7,8,8,10], 8))
print(searchRange([5,7,7,8,8,8,8,8,9,10,11], 8))
print(searchRange([5,7,7,8,8,10], 6))

print(searchRange([], 0))

print(searchRange([5,7,7], 128))

print(searchRange([5,7,7,8,8,10,11,11,11,22], 5))