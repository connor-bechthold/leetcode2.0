#My solution
#O(mn) time, O(mn) space
class Solution:
    #Strategy: DP. Since we can only move down and right, we know all squares
    #down the top and left side can only be apart of 1 unique path each
    #So, we can initilaize those all to 1
    #The rest of the spots are then just simply the sum of the square to its left and the square above
    #At the end, the number of unique paths will be in the bottom right square
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for i in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]
    
#Ideal solution (reduce space to O(n))
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        curr = prev = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                curr[j] = curr[j - 1] + prev[j]
            prev = curr
            curr = [1] * n
        return prev[n - 1]
    
#If you're really cool you don't even need the second array
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        curr = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                curr[j] += curr[j - 1]
        return curr[n - 1]
