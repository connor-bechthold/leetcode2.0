#My solution
#O(n) time, O(n) space
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        lookup = {}
        
        #Add each number to the hash table
        for num in nums:
            lookup[num] = 1
            
        #Loop through a range of every possible number
        #If a number does not exist, return that number
        for i in range(0,len(nums) + 1):
            if i not in lookup:
                return i

#Ideal solution
#O(n) time, O(1) space
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n = len(nums)
        #Get the sum of the current list
        total = 0
        for num in nums:
            total += num
        
        #Summation formula for n distinct numbers (use floor division for ints)
        actual = (n * (n+1)) // 2
        
        #The difference in these two values will be the number we're missing
        return actual - total
