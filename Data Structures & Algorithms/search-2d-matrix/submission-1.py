class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        numRows = len(matrix)
        numCol = len(matrix[0])
        bottom = 0
        top = numRows-1
        middleRow = (top+bottom)//2
        while bottom <= top:
            middleRow = (top+bottom)//2
            if(target < matrix[middleRow][0]):
                top = middleRow-1
            elif(target > matrix[middleRow][-1]):
                bottom = middleRow+1
            else:
                break
        if not bottom<=top:
            return False
        
        left = 0
        right = len(matrix[middleRow])-1
        while left <= right:
            middleCol = (left+right)//2
            if(target<matrix[middleRow][middleCol]):
                right = middleCol-1
            elif(target>matrix[middleRow][middleCol]):
                left = middleCol+1
            else:
                return True
        return False