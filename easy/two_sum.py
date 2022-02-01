#My solution, ideal solution
#O(n) time, O(n) space
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Strategy: Keep a lookup table while iterating through list
        #Keep track and store the difference between the target and the current
        #val, storing its index as well
        #At each iteration, we will look for that difference to appear in the table
        #If we find a match, we know the two numbers at those two indexes add to the target
        lookup = {}
        for i in range(0, len(nums)):
            if target - nums[i] in lookup:
                return[lookup[target - nums[i]], i]
            lookup[nums[i]] = i
