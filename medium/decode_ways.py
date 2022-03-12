#My solution, sorta ideal solution (could easily make this O(1) space)
#O(n) time, O(n) space
class Solution:
    
    #Strategy: Bottom up dp, kinda similar to climbing stairs where we're constantly looking back 1 and 2 spots in our dp array
    #Overall strategy: At each position, check the value at that position is greater than 0. If it is, then we can increment the number of ways by the number of ways we found in the previous position
    #Since we can range up to 26 (2 digits), we also check add the previous char val to our current one. If that value is >= 10 and <= 26, then that is also a valid pattern, and we increment the number of ways by the number of ways we found 2 positons back
    #Example: [2, 3, 1] (2 ways, 231, 23 1))
    #Initalize our dp array to [1, 0, 0, 0]
    #We start at the beginning. 2 is greater than 0, so we have [1, 1, 0, 0]
    #We move to 3. We see that three is greater than 0, so that means adding 3 to the combination 1 spot back is valid. [1, 1, 1, 0]
    #We also look at the double digit number. We see that adding 3 to 2 gives us 23, which is valid
    #So, we add the number of ways we saw before the 23, as that's a valid pattern (which is why we have that extra 1 initialized at the start). [1, 1, 2, 0]
    #Move to 1. 1 is greater than 0, so we add the prev # of ways. [1, 1, 2, 2]
    #We find the two digit number. This is 31, which is NOT valid. SO, we do not add the number of ways we see in index 1.
    #Return 2, which is the number of ways.
    
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 1 if s[0] != '0' else 0
        
        for i in range(2, len(s) + 1):
            
            single = s[i-1]
            double = s[i-2:i]
            
            if single > '0':
                dp[i] += dp[i-1]
            if double >= '10' and double <= '26':
                dp[i] += dp[i-2]
        
        return dp[len(s)]
