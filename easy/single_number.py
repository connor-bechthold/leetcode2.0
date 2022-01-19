#My solution
#O(n) time, O(n) space
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #Iterate through list, adding num to hash table if it doesn't exist
        #If it does, remove it, as we've already seen it
        #The remaining value in the hash table will be the missing number
        lookup = {}
        for i in range(0, len(nums)):
            if nums[i] not in lookup:
                lookup[nums[i]] = 1
            else:
                lookup.pop(nums[i])
        return next(iter(lookup))
        
#Ideal solution
#O(n) time, O(1) space
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        #Utilise XOR
        #Note that order of XOR does not matter, and the XOR of the same number is 0
        #Also, the XOR of 0 is the number 0 is XOR'ed with
        #Thus, if we XOR every number in the list together with 0, we get the missing number
        
        value = 0
        for i in range(0, len(nums)):
            value ^= nums[i]
        return value
