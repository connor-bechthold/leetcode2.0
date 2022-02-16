#My solution, ideal solution
#Time: O(n * n!) - n! is the number of combinations there are for n distinct numbers
#Space: O(n)
class Solution:
    
    #Strategy: Backtrack and build each combination from the bottom up
    #For each index in our list we build, we will also keep track of the numbers that we have available
    #In order to this, we will remove the current number we have used from the nums list, and pass it along with one less element
    #Once we don't have anymore elements left, we know we have a new combination, and can add it to the output
    #We then push the last element we used into the correct position, and continue
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.construct(nums, [], [])
        
    def construct(self, nums, curr, ret):
        
        if len(nums) == 0:
            ret.append(curr)
        for i in range(0, len(nums)):
            nex = curr + [nums[i]]
            temp = nums.pop(i)
            self.construct(nums, nex, ret)
            nums.insert(i, temp)
        return ret
