def duplicateZeros(arr) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        curIdx, length = 0, len(arr)
        while curIdx < length:
            if arr[curIdx] == 0:
                for i in range(len(arr)-1, curIdx, -1):
                    arr[i] = arr[i-1]
                curIdx += 1
            curIdx += 1
            

duplicateZeros([1,0,2,3,0,4,5,0])
print(help(range))
                    