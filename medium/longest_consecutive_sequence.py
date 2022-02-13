#Ideal solution
#O(n) time, O(n) space
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        #Strategy: Construct a hash set of the values of the list
        #For each of these numbers, check if there's a number in the set that is one less than the current number
        #If there is, do nothing and continue
        #Eventually, we will reach a number in which there isn't a value that is one less than that value, indicating that we are at the start of a sequence (of minimum length 1)
        #Working our way up to the end of the sequence, we keep track of the length of it and keep track of a max sequence length along the way
        #Tricky part: This looks O(n^2)
        #Take [5,4,3,2,1]
        #We go over 5,4,3,2 and do nothing, as there's values one lower than each one
        #When we get to 1, we iterate through 1 -> 5, and return the max sequence
        #This looks O(n^2), but looking closely, we only iterate over each value a MAXIMUM of 2 times. Thus, this is actually O(2n), which is just O(n)
        numSet = set(nums)
        
        longestSequence = 0

        for num in numSet:
            if (num - 1) not in numSet:
                currentSequence = 1
                currentNum = num
                while (currentNum + 1) in numSet:
                    currentSequence += 1
                    currentNum += 1
                longestSequence = max(longestSequence, currentSequence)
                
        return longestSequence
