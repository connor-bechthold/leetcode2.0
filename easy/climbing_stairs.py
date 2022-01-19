#My solution
#O(n) space
class Solution:
    def climbStairs(self, n: int) -> int:
        
        #DP approach
        #Define our base cases: 1 way to take 1 step, and 2 ways to take 2 steps
        #Now, working our way up, to take n steps
        #There are k distinct ways to take n-1 steps, and then each time take 1 step to get to n steps
        #There are j distinct ways to take n-2 steps, and then take 2 steps to get to n steps
                
        #Base cases
        if n == 1:
            return 1
        if n == 2:
            return 2
    
        dp = [0 for i in range(0, n + 1)]
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]
    
#Ideal solution
#O(1) space
class Solution:
    def climbStairs(self, n: int) -> int:
        
        #Same as above, no need to store intermediate result
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        first = 1
        second = 2
        
        for i in range(3, n + 1):
            following = first + second
            first = second
            second = following
            
        return following
    
#Another ideal solution, top down
#O(1) space
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.climbStairs(n - 1) + self.climbStairs(n - 2)
