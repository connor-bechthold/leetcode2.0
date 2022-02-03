#My solution
#O(n) time, O(n) space
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Strategy: Create a prefix and suffix array, and then at each index, the product at that index is the prefix number located before that index times the suffix number located after that index
        #Essentially, the value at a certain index is the product of all the numbers to the left of that index multiplied by the product of all the numbers to the right of that index
        prefix = [0] * len(nums)
        prefix[0] = nums[0]
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i]

        suffix = [0] * len(nums)
        suffix[len(nums) - 1] = nums[len(nums) - 1]
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i]
        
        output = [0] * len(nums)
        for i in range(0, len(nums)):
            if i == 0:
                output[i] = suffix[i + 1]
            elif i == len(nums) - 1:
                output[i] = prefix[i - 1]
            else:
                output[i] = prefix[i - 1] * suffix[i + 1]
                
        return output
    
#Ideal solution
#O(n) time, O(1) space (as output array does not count as extra space)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Same solution as above, however we do everything in place in the output array
        output = [1] * len(nums)
        prefix_sum = nums[0]
        for i in range(1, len(nums)):
            output[i] *= prefix_sum
            prefix_sum *= nums[i]
            
        suffix_sum = nums[len(nums) - 1]
        for i in range(len(nums) - 2, -1, -1):
            output[i] *= suffix_sum
            suffix_sum *= nums[i]
            
        return output
