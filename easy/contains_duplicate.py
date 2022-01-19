#My solution, ideal solution
#O(n) time, O(n) space
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        #Keep adding numbers in the list in hash table
        #If we find a number in the table, return True, as it's a duplicate
        #Otherwise, return False
        lookup = {}
        for number in nums:
            if number in lookup:
                return True
            lookup[number] = 1
        return False
