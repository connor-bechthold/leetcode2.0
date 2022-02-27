#My solution, ideal solution
#O(n) time, O(1) space
class Solution:
    
    #Strategy: Similar to max subarray, but we keep track of a current maximum AND a current minimum, as we are dealing with negative numbers
    #We set the global max, local max, and local min equal to the first value in the list
    #At each iteration, we do a couple things:
    #Store our currentMax in a var called prevMax - this is because we need to to use the currentMax in our calculation of the currentMin, however, the currentMax is updated before the currentMin, so we store the intermediate result
    #We first calculate our current max, which is the max of the current number "n" we're at, n * the current max, and n * the current min
    #Examples: [-1, 8], we start at index 1, and the max is just 8 ("n")
    #          [2, 8], the currentMax starts at 2, multiplying by 8 gives us 16
    #          [-2,4,4,-8], once we reach -8, the currentMax will be 16, and the currentMin will be -32. Clearly, -32 * -8 gives us the biggest max
    #We then calculate the current min, is the min of the same three cases
    #Examples: [1, -8], the min is simply -8 ("n")
    #          [2, 2, -2], once we reach -2, the currentMin will be the currentMax(4) * "n", which is -8
    #          [-2, 2, 3], once we reach 3, the currentMin will be the currentMin(-4) * "n", which is -12
    #Finally at the end, we update the global max with our current max if needed
    def maxProduct(self, nums: List[int]) -> int:
    
        ans = currentMax = currentMin = nums[0]
        
        for i in range(1, len(nums)):
            
            prevMax = currentMax
              
            currentMax = max(currentMax * nums[i], currentMin * nums[i], nums[i])
            currentMin = min(prevMax * nums[i], currentMin * nums[i], nums[i])
                        
            ans = max(ans, currentMax)
 
        return ans
