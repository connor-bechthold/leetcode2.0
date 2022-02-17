#My solution, ideal solution
#O(n*n!) time, O(n) space
class Solution:
    #Strategy: Identical to permutations, but we need to sort the list and for each element we iterate over, check if the previous element is the same
    #If it's the same, we've already created permutations for it, so there's no need to do it again
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        return self.construct(nums, [], [])
        
        
    def construct(self, nums, curr, ret):
        
        if len(nums) == 0:
            ret.append(curr)
        
        for i in range(0, len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            nex = curr + [nums[i]]
            temp = nums.pop(i)
            self.construct(nums, nex, ret)
            nums.insert(i, temp)
            
        return ret
