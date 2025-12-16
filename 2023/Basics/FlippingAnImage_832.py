# Status: Good

class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        """
        Reverse each row 
        Invert each element
        """
        ilen = len(image)
        for row in range(ilen):
            for col in range(ilen):
                if image[row][col] == 0:
                    image[row][col] = 1
                else:
                    image[row][col] = 0
            #image[row] = image[row][::-1]
            image[row].reverse()
        return image
        
solve = Solution()
print(solve.flipAndInvertImage(image = [[1,1,0],[1,0,1],[0,0,0]]))
print(solve.flipAndInvertImage(image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))