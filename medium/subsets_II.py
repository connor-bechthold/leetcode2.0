#My solution, ideal solution
#O(n * 2^n) time, O(n) space
class Solution:
    #Strategy: Similar to subsets, but we have to sort the input array
    #This is done to prevent multiple subsets that contain the same elements, but are in different order
    #For ex. [4,4,4,1,4]. Without sorting, we would add [1,4] and [4,1], which are the same subset
    #Now, in order to prevent duplicates, we check to see if the current element we're attemping to add to our current subset is the same element as the previous one, ONLY if our index is greater than our pos index
    #This is done for ex. [1,1,2]
    #We first add [1], but don't want to add [1] again. This is avoided, as the second 1 occurs when pos is 0 and i is 1, so it's never added
    #When [1] is our current path, pos starts at 1. Even though this means that the index at i and i - 1 are both one, pos starts at 1 and i also starts at one
    #So, we add [1,1], which is what we want
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        return self.construct(nums, 0, [], [])
        
    def construct(self, nums, pos, curr, ret):
        ret.append(curr)
        for i in range(pos, len(nums)):
            if i > pos and nums[i] == nums[i - 1]:
                continue
            self.construct(nums, i + 1, curr + [nums[i]], ret)
        return ret
