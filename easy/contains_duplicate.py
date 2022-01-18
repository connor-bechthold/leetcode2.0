#O(n) time, O(n) space

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        lookup = {}
        for number in nums:
            if number in lookup:
                return True
            lookup[number] = 1
        return False
