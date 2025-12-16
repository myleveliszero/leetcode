def findClosestElements(arr, k: int, x: int):
        left, right = 0, len(arr)-1 
        while left <= right:
            mid = left + (right-left)//2    
            if arr[mid] < x:
                left = mid+1
            else: 
                right = mid-1
    
        if left == len(arr):
            left -= 1
        
        mid = left
        if mid==0:
            return arr[:k]
        elif mid == len(arr)-1:
            return arr[-k:]
        a, b = mid-1, mid
        # print('mid: ', left)    
        for i in range(1, k+1):
            if b == len(arr):
                a -= k-i
                return arr[a:b]
            elif a == 0:
                b += k-i
                return arr[a:b]
            if x - arr[a] <= arr[b]-x:
                a -= 1
            else: 
                b += 1

        return arr[a+1:b]


# print(findClosestElements([1,2,3,4,4,4,4,5,5], k = 3, x = 3))  

print(findClosestElements([1,1,2,3,4,5,5,6,6,8,8], k = 4, x = 7))  
# print(findClosestElements([1,1,2,3,4,55,55,56,56,58,58], k = 4, x = 5))
print(findClosestElements([1,1,2,3,4,55,55,56,56,58,58], k = 4, x = 55))        
print(findClosestElements([1,2], k = 4, x = 5))
print(findClosestElements([1,2], k = 4, x = 2))
print(findClosestElements([1], k = 4, x = 143))
print(findClosestElements([1,2,3,4,5], k = 4, x = 1))                 
print(findClosestElements([1,2,3,4,5], k = 4, x = 0))

        