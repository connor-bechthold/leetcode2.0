#My solution, ideal solution
#O(n) time, O(1) space
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        #Keep track of the size of the max subarray, and the current subarray
        #Loop through the list, adding the current number to the current total if it gives a greater value than just setting the current value to that number
        #After every number, update the max total we've seen before, and return it at the end
        
        maximum = current = float(-inf)
        for num in nums:
            if num > (num + current):
                current = num
            else:
                current += num
            maximum = max(current, maximum)
            
        return maximum
    
#DP solution
#O(n) time, O(n) space
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        #Same approach as above, just with storing intermediate results
        dp = [0]*len(nums)
        for i in range(0, len(nums)):
            if i == 0:
                #Base case
                dp[i] = nums[i]
            else:
                dp[i] = max(dp[i-1] + nums[i], nums[i])
        
        return max(dp)
