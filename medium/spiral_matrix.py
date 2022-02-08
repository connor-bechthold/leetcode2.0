#O(nm) time, O(1) space
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        #Strategy: Keep four vars to track where we need to start and stop on each row/column iteration
        #For ex. we initialize "rowBegin" to 0, as we need to start moving along the 0th row
        #After we do this, we increment rowBegin by 1, as we've covered that row of the spiral
        #We repeat this same process with the other 3 sides, modifying one of the four boundary vars each time
        #Within the loop, move right, down, left, and up until one of the begin vars is greater than the end vars, as that's when we know we are at the end of the spiral, since they are getting closer each time
        #We need to be extra careful when going left and up
        #Take a matrix with one row and three columns [[1, 2, 3]]
        #We move right, and add 1, 2, 3 to arr
        #Since rowBegin and rowEnd are both 0 initially, after adding 1, the down loop is not executed
        #After this, colEnd takes a val of 1, which happens to be greater than the value of colBegin, 0
        #The problem is, we don't want to go left anymore, since there's only one row
        #So, before we go left, we see check that rowBegin <= rowEnd
        #Here, RB is 1 and RE is 0, so we don't go left
        #The same goes for [[1], [2], [3]]. We need to check that colBegin <= colEnd, or we will go up when we don't need to
        
        rowEnd = len(matrix) - 1
        colEnd = len(matrix[0]) - 1
        rowBegin = colBegin = 0
        i = j = 0
        arr = []
        
        while rowBegin <= rowEnd and colBegin <= colEnd:
            #Move right
            while j <= colEnd:
                arr.append(matrix[i][j])
                j += 1
            
            j = colEnd
            rowBegin += 1
            i = rowBegin
            
            #Move down
            while i <= rowEnd:
                arr.append(matrix[i][j])
                i += 1
                
            i = rowEnd
            colEnd -= 1
            j = colEnd
            
            #Move left
            if rowBegin <= rowEnd:
                while j >= colBegin:
                    arr.append(matrix[i][j])
                    j -= 1
                
            j = colBegin
            rowEnd -= 1
            i = rowEnd
            
            #Move up
            if colBegin <= colEnd:
                while i >= rowBegin:
                    arr.append(matrix[i][j])
                    i -= 1
            
            i = rowBegin
            colBegin += 1
            j = colBegin
            
        return arr
