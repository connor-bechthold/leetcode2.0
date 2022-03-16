#My solution
#O(n^2) time, O(n) time
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        #Strategy: Similar to longest increasing subsequence
        #Length stores the max length subsequence at each index (like usual)
        #Count stores the amount of times the max length subsequence at that index occurs
        #Once we determine the max length of the increasing subsequence, we can simply find the indexes that that value occurred at, and use each index to map the amount of times it occurred that iteration
        #We simply add all these sums, which gives the number of longest increasing subsequence
        
        if len(nums) == 1:
            return 1
        
        length = [1] * len(nums)
        count = [1] * len(nums)
        
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    curr = length[j] + 1
                    if curr == length[i]:
                        count[i] += count[j]
                    elif curr > length[i]:
                        count[i] = count[j]
                    length[i] = max(length[i], curr)
         
        maxLen = max(length)
        return sum([count[k] for k in range(0, len(length)) if length[k] == maxLen])
