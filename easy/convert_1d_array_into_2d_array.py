#My solution
#O(n) time, where n is the length of the list
#O(n * m) space
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        
        #Not much to explain, just check if the 2D array is valid and if it is, make the conversion
        if len(original) != n * m:
            return []
        arr = [[0]*n for i in range(m)]
        for i in range(0, m):
            for j in range(i * n, (i * n) + n ):
                arr[i][j - n * i] = original[j]
        return arr
    
#Simpler solution
#O(n) time, where n is the length of the list
#O(n * m) space
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != n * m:
            return []
        arr = [[0]*n for i in range(m)]
        for i in range(0, len(original)):
            arr[i // n][i % n] = original[i]
        return arr
