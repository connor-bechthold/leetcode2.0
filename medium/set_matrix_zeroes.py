#My solution
#O(mn) time, O(m + n) space
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        #Strategy: Store arrays of rows and columns that need to be zeroed
        #Once this is done, set those rows and columns to zeroes
        m = len(matrix)
        n = len(matrix[0])
        rows = []
        cols = []
        
        for i in range(0, m):
            for j in range(0, n):
                if matrix[i][j] == 0:
                    if i not in rows:
                        rows.append(i)
                    cols.append(j)
                    
        for row in rows:
            for col in range(0, len(matrix[row])):
                matrix[row][col] = 0
        
        for col in cols:
            for row in range(0, len(matrix)):
                matrix[row][col] = 0
                
               
#Ideal solution
#O(mn) time, O(1) space
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        #Strategy: If a matrix entry is 0, set the first entry of that row and that col to 0 to indicate that the the entire row and col need to be zeroed
        #That way, after iteration is done, the first entry of each row and col can be iterated through, and zeroed out
        #NOTE: A problem arises if a 0 initially appears in the first entry of a row or col
        #By the algorithm, this will always trigger the [0][0] entry to be zero
        #When we're zeroing out at the end and [0][0] is zero, we have no idea whether that means to zero out the row, col, or both
        #So, we avoid this by doing a check at the beginning, and setting the is_row and is_col vars to true if an entry like this occurs
        #When we're zeroing out like normal, we completely avoid the [0][0] entry
        #After this is done, we then zero out the first row/col or both, depending on the value of the two bools
        
        m = len(matrix)
        n = len(matrix[0])
        
        is_col = is_row = False
        
        for i in range(0, m):
            for j in range(0, n):
                if matrix[i][j] == 0:
                    if i == 0:
                        is_col = True
                    if j == 0:
                        is_row = True
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                    
        for i in range(1, m):
            if matrix[i][0] == 0:
                for col in range(0, n):
                    matrix[i][col] = 0
                    
        for j in range(1, n):
            if matrix[0][j] == 0:
                for row in range(0, m):
                    matrix[row][j] = 0
                
        if is_col:
            for col in range(0, n):
                matrix[0][col] = 0
            
        if is_row:
            for row in range(0, m):
                matrix[row][0] = 0  
