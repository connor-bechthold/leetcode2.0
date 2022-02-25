#My solution, ideal solution
#O(n) time, O(1) space
class Solution:
    
    #Strategy: Essentially the same as the first house robber
    #We can use the same logic
    #The circular condition restricts us to either visiting the first house or the last house, but not both
    #So for ex. if we have [1,2,3,4], we can evaluate [1,2,3] and [2,3,4]
    #We can plug those two different lists into our original house robber solution (as these lists don't have any abnormal restrictions) and take the max as our answer
    
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        def rec(n, houses):
            
            if len(houses) == 1:
                return houses[0]
            
            first = nex = 0
            second = houses[0]
            
            for i in range(1, len(houses)):
                nex = max(houses[i] + first, second)
                first = second
                second = nex
                
            return nex
        
        n = len(nums)
        
        return max(rec(n - 1, nums[1:]), rec(n - 1, nums[:n-1]))
