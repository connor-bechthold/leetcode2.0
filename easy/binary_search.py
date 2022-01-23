#My solution, ideal solution
#O(log(n)) time, O(n) space
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        #Basic binary search, try not to be a clown and forget this
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        
        return -1
