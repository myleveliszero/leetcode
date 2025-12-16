def duplicateZeros(arr) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        curIdx, length = 0, len(arr)
        nums = []
        while curIdx < length: 
            
            if arr[curIdx] == 0:
                nums.append(0)
                nums.append(0)
            else:
                nums.append(arr[curIdx])
            
            curIdx += 1                    
        for i in range(length):
            arr[i] = nums[i]
                         
        

duplicateZeros([1,0,2,3,0,4,5,0])
# print(help(range))
                    