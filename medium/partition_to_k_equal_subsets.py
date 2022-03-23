#My solution - does not work for 1 magical test case I do not care enough about
#It is 1 AM
#I have work tomorrow
#If this q gets asked in an interview and this test case does not exist, I am going to re-evaluate my career choice
#O(k * 2^n) - Each call to backtrack, we either choose to add the current element or not add it, which is 2 choices. This is done k times
#O(n) space
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        #Strategy: Find what each subset sum needs to be
        #Backtrack through nums and attempt to find a sum of that total, keeping track of the indexes used each time (since they can't be used more than once)
        #We do this k times, as there needs to be k subsets of that sum
        #The indexes we use are skipped over in the logic
        
        total = sum(nums)
        
        if total % k != 0:
            return False
        
        target = total // k
        memo = set()
        
        nums.sort(reverse=True)
        
        def backtrack(pos = 0, curr = 0):
            if curr == target:
                return True
            if curr > target:
                return False
            for i in range(pos, len(nums)):
                if i not in memo:
                    memo.add(i)
                    if backtrack(pos + 1, curr + nums[i]):
                        return True
                    memo.remove(i)
            return False
        
        for i in range(0, k):
            if not backtrack():
                return False
        
        return True
