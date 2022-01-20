#My solution, ideal solution
#O(n) init, O(1) query,  O(n) overall, O(n) space
class NumArray:
    def __init__(self, nums: List[int]):
        #Each value at the nth index stores the sum of the value at the n-1th index plus the value at the nth index
        self.nums = nums
        self.dp = [0]*len(nums)
        for i in range(0, len(nums)):
            if i == 0:
                self.dp[i] = nums[i]
            else:
                self.dp[i] = self.dp[i - 1] + nums[i]
        

    def sumRange(self, left: int, right: int) -> int:
        #Note that the value at index n is the sum of the values at indexes n-1, n-2, ... , 0
        #Since the right index >= left index, the right index includes the sum from right, .... , left, ...., 0.
        #We want the sum from left, ...., right
        #So, we can take the value of the dp list at the right index, and subtract the index 1 spot behind the left index from it
        #This gives the sum from index left to right
        if left == 0:
            return self.dp[right]
        else:  
            return self.dp[right] - self.dp[left - 1]
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
