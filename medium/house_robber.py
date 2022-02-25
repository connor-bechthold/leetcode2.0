#My solution, not ideal solution
#O(n^2) time, O(n) space
class Solution:
    #Strategy: Keep track of the max we can collect at each house
    #This value is the value of the current house plus the max of the values we can get at the houses before this one (excluding the one down one index)
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        dp[0] = nums[0]
        dp[1] = nums[1]
        
        for i in range(2, len(nums)):
            dp[i] = nums[i] + max(dp[0:i-1])
            
        return max(dp)
                
#Another solution
#O(n) time, O(n) space (recursive memoization, top down)
class Solution:
    #Strategy: At each house, we can either skip the current house, or rob the current house and move two houses
    #So, at each house, we take the max of 2 houses down plus, the current house, or the previous house
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def rec(n):
            if n < 0:
                return 0
            if n in memo:
                return memo[n]
            num = max(nums[n] + rec(n - 2), rec(n - 1))
            memo[n] = num
            return num
        
        return rec(len(nums) - 1)
    
#Another solution O(n) time, O(n) space (iterative tabulation, bottom up)
class Solution:
    def rob(self, nums: List[int]) -> int:
        #Strategy: Similar to top down, however our dp list has to be initialized with a 0 in the first index
        #So for ex, [8,1,1,9] outputs [0,8,8,9,17]
        #If we didn't do this: [8,1,9,10] <- NOT GOOD
        if len(nums) == 1:
            return nums[0]
        
        dp = [0] * (len(nums) + 1)
        dp[0] = 0
        dp[1] = nums[0]
        
        for i in range(1, len(nums)):
            dp[i + 1] = max(nums[i] + dp[i - 1], dp[i])
            
        return dp[len(nums)]
    
#Ideal solution
#O(n) time, O(1) space (iterative bottom up, no tabulation)
class Solution:
    #Strategy: Same as above solution, however, there's no need to tabulate!
    #We can use two temporary variables to accomplish the same algorithm, which allows us to have constant space
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        one = nex = 0
        two = nums[0]
        
        for i in range(1, len(nums)):
            nex = max(nums[i] + one, two)
            one = two
            two = nex
            
        return nex
