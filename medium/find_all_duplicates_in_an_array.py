#My solution, ideal solution
#O(n) time, O(1) space
class Solution:
    
    #Solution: Take advantage of the range of nums
    #Each num can be mapped to an index that is one below its value
    #For each value we iterate over, subtact its value by one, and set the index it maps to as negative (to indicate it already exists)
    #If we reach a duplicate, the index it maps to will already be negative
    #We check for that, and if true, add it to the output array
    def findDuplicates(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(0, len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] < 0:
                output.append(index + 1)
            else:
                nums[index] *= -1
                
        return output
