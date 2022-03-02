#My solution
#O(n^2) time, O(n) space
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        #Strategy: DP approach, keep an array storing the longest increasing subsequence at that position
        #As we iterate through nums, we'll check each element before and if it's less than the current element, it's apart of an increasing subsequence, so we store the max of what's currently at that index with the smaller number's longest + 1 (since our current n number will be apart of it)
        #At the end, return the max
        
        if len(nums) == 1:
            return 1
        
        dp = [1] * len(nums)
        
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
    
#Ideal solution
#O(nlog(n)) time, O(n) space
class Solution:
    #Strategy: Sub is an array storing the smallest "tail" of subsequence length i + 1 for each index i of the arrau
    #For ex [1,4,2,3], smallest tail for i = 1 is [1,2], so 2, not [1,3], as 3 > 2
    #Two cases:
    # - If our current element is greater than the last element in sub, we append it to increase the subsequence
    # - Else, replace the smallest element in sub which happens to be greater than or equal to the current element we're on
    #Since sub is going to be sorted, we can use binary search to find the position and replace the appropriate value in the array
    #At the end, the length of this array is the length of the longest subsequence
    #For example [4,5,6,3] would result in [3,5,6] because
    #Length 1: [3]
    #Length 2: [4,5]
    #Length 3: [4,5,6]
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        def binarySearch(nums, val):
            start = 0
            end = len(nums) - 1
            while start <= end:
                mid = (start + end) // 2
                if nums[mid] == val:
                    return mid
                elif nums[mid] < val:
                    start = mid + 1
                else:
                    end = mid - 1
            #Start will give us the position of the smallest element greater than val
            return start
        
        sub = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > sub[len(sub) - 1]:
                sub.append(nums[i])
            else:
                pos = binarySearch(sub, nums[i])
                sub[pos] = nums[i]
                
        return len(sub)
