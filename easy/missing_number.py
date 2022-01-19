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
    
#Alternative ideal solution
#O(n) time, O(1) space

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        #Apply XOR to every value in the range (0, n) with the values in the list.
        #The resulting value will be the missing number
        start = len(nums)
        for i in range(0, len(nums)):
            start ^= i ^ nums[i]
        
        return start
    
