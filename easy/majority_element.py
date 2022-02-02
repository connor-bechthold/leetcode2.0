#O(n(log(n))) time, O(1) space
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #Strategy: Keep a counter and iterate through a sorted version of the list
        #The counter increments for every consecutive element we pass over
        #If that counter reaches a value over the majority threshold, we return the number as its the majority element
        #The counter resets everytime the current element is not the same as the next element
        maj = floor(len(nums) / 2)
        nums.sort()
        counter = 1
        for i in range(0, len(nums)):
            if counter > maj:
                return nums[i]
            elif nums[i] == nums[i + 1]:
                counter += 1
            else:
                counter = 1
    
#O(n) time, O(n) space
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #Keep a hash map and return the maj element once the key value pair in the hash table reaches a value greater than the len(nums) / 2
        maj = floor(len(nums) / 2)
        lookup = {}
        for i in range(0, len(nums)):
            if nums[i] not in lookup:
                lookup[nums[i]] = 1
            else:
                lookup[nums[i]] += 1
            if lookup[nums[i]] > maj:
                return nums[i]

#O(n) time, O(1) space
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #Cool solution, keep track of a current candidate as we iterate through the list
        #If we see that canadidate, increment by one, else decrement by one
        #Once that candidate is decremented to zero, it is replaced by a new candidate, which is the number at the current index
        #At the end, the current candidate will be the majority element
        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
                count += 1
            elif num == candidate:
                count += 1
            else:
                count -= 1
        return candidate
