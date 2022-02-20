#My solution
#O(2^n) time (worst case), O(n * target) space (don't really understand space, come back later)
class Solution:
    
    #Strategy: Keep track of the current position we're at in the array, along with the current sum
    #At each position, we will call the function with the positive and negative value of the number added to the current sum
    #This way, we can exhaust every sum
    #Once our position reaches the length of nums, we can check if we have a valid sum. If we do, we can return 1, else, 0
    #At each positin, the number of ways that satisfy the target is the sum of the number of ways by subtracting and adding the current numbet to the sum, and increasing position
    #However, a simple print statement will make you realize there's a lot of overlap in this solution
    #Once we're at a certain index, and have a certain current sum, we can store the number of ways there are to construct the target at this current step
    #That way, at the start of each recursive call, we can check is we've already calculated this previously, which speeds up the process
    
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        return self.construct(nums, target, 0, 0, {})
        
        
    def construct(self, nums, target, pos, curr, memo):
        
        if (pos, curr) in memo:
            return memo[(pos, curr)]
        
        if pos == len(nums):
            if curr == target:
                return 1
            return 0
        
        positive = self.construct(nums, target, pos + 1, curr + nums[pos], memo)
        negative = self.construct(nums, target, pos + 1, curr - nums[pos], memo)
                
        memo[(pos, curr)] = positive + negative
        return positive + negative
