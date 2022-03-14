#My solution - Top down DP
#O(n^2) time, O(n) space
class Solution:
    #Strategy: Work from the second last item in the list to the front
    #By default, the last item in the list will be True, as it is the end
    #At each element, we find the max length we can jump (to the end of the list or the current number, incase the current number goes over the end of the list)
    #Iterating down from that step, find if a spot in dp is True. If it is, set the current spot to True and break
    #The solution will be the value at the front of dp, or, where we jump from
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[len(nums) - 1] = True
        
        for i in range(len(nums) - 1, -1, -1):
            maxStep = min(nums[i], len(nums) - i - 1)
            for j in range(maxStep, 0, -1):
                if dp[i + j]:
                    dp[i] = True
                    break
        return dp[0]
    
#Alternative solution, similar to above approach but much more efficient
#O(n) time, O(1) space
class Solution:
    #Strategy: Keep track of the smallest index we come across that resuls in a valid path
    #By default, this index is the last index in the list
    #Then, starting from the second last item in the list and moving to the second index,
    #We simply check whether the current number (jump length) plus the current index is greater than or equal than our min index
    #If it is, then we replace the min index with the current index
    #At the end, we simply return if our starting number is greater than or equal to the min index we need to jump in order to reach the end
    def canJump(self, nums: List[int]) -> bool:
        minPos = len(nums) - 1
        for i in range(len(nums) - 1, 0, -1):
            if i + nums[i] >= minPos:
                minPos = i
        return nums[0] >= minPos
