#This is based off the 0/1 knapsack problem
#O(n * sum) time, O(n * sum) space
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        #The gist is that we just need to find x amount of numbers that sum to half the total of nums
        #If we can find one, then it is guaranteed that the sum of the rest will equal the total, since the total needs to be even 
               
        total = sum(nums)
        
        #If the total isn't even, equal partitions can't be achieved
        if total % 2 != 0:
            return False
        
        #Our target for each partition is the total divided by 2
        target = total // 2
        
        #Rows - values in nums plus zero row
        #Columns - Sum up to the target (halfway)
        dp = [[False] * (target + 1) for i in range(0, len(nums) + 1)]
        dp[0][0] = True
        
        #To make sum 0, we can simply pick no numbers
        for i in range(1, len(nums) + 1):
            dp[i][0] = True
            
        #Can't make a sum greater than 0 by only picking 0
        for j in range(1, target + 1):
            dp[0][j] = False
            
        #For each slot we have two options
        #DO NOT PICK: dp[i - 1][j]: We simply copy over the result from excluding that number and look at the previous result for the same sum
        #PICK: dp[i - 1][j - nums[i - 1]]: We again remove that number, but the current sum will decrease by the current number we have chose
        
        for i in range(1, len(nums) + 1):
            for j in range(1, target + 1):
                dp[i][j] = dp[i - 1][j]
                if j - nums[i - 1] >= 0:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
                    
        print(dp)
        return dp[len(nums)][target]
    
    
#Optimized solution
#O(n * sum) time, O(sum) space
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        total = sum(nums)
        
        if total % 2 != 0:
            return False
        
        target = total // 2
        
        dp = [False] * (target + 1)
        dp[0] = True
        
        #Almost identical strategy to above
        #We still loop through each number in nums
        #For each one of these numbers, we subtract its value from each sum in the array, as long as the sum is >= num
        #If we find that the resulting sum value in dp is true, then we know that the current sum can be constructed from smaller sums, and set the current sum to true
        #We return dp at our target sum, as if we can construct this sum within the array, then it is guaranteed that we can construct equal partitions
        for num in nums:
            for j in range(target, -1, -1):
                if j - num >= 0:
                    dp[j] = dp[j] or dp[j - num]
                    
        return dp[target]
