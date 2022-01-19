#My solution
#O(n) time, O(n) space
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        #Strategy - Copy list over to hash table, loop range from 1-n, 
        #checking if the number exists. If it doesn't, add to output
        lookup = {}
        n = len(nums)
        for num in nums:
            lookup[num] = 1
        
        output = []
        for i in range(1, n+1):
            if i not in lookup:
                output.append(i)
                
        return output


#Ideal Solution
#O(n) time, O(1) space
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        #Loop thrugh list and get an index from each value (num - 1)
        #Go to that index in the list, and make the value there negative
        #At the end, if a value at an index is positive, we now that the
        #number with the value index + 1 does not exist, or it would be negative
        
        n = len(nums)
        for i in range(0, n):
            current = abs(nums[i]) - 1 #abs, could be already negative
            nums[current] = -abs(nums[current])
        
        return [i + 1 for i in range(0, n) if nums[i] > 0]
