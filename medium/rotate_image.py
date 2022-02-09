#Ideal solution
#O(n^2) time, O(1) space
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        #Strategy: Take the transpose of the matrix, which for a square matrix, is swapping vals across the diagonal
        #Then we vertically flip the transpose to get the clockwise rotated matrix
        
        #Transpose: Start at each diagonal square, work down and right, swapping vals each time
        n = len(matrix)
        for i in range(0, n):
            for j in range(i, n):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        
        #Vertical flip: Go through each row, setting a pointer at each end
        #Swap each val, and move one step to the middle on each side
        for i in range(0, n):
            for j in range(0, n // 2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][n - j - 1]
                matrix[i][n - j - 1] = temp
