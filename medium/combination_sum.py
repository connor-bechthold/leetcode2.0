#My solution, ideal solution
#The length of each combination is at max (target / min(candidate)) in length (k)
#An upper bound on the amount of combinations we have is len(candi)^k
#Ex [1,2,3] Target 1000, [1,1,1,1,....] 1000 times. For each of these elements, we have, to iterate through every element of the list. Thus, len(candi)^k
#Thus, time complexity is O(k * len(candi)^k)
#Space complexity is O(target / min(candidate))
class Solution:
    
    #Strategy: Iterate through the list and for each item, only examine the current element and beyond when adding to the current list
    #We will keep track of the current position we're at, the current sum we've reached, and also the current combination we're at
    #At each step, we will add the current value to the current list, incremenent our current total, and call the function on the new current list
    #After we've exhausted the options, we decrement our current total and move to the next element
    #We will stop the current iteration when the current sum is >= to the target
    #If it's equal, add it to the return list, else, do nothing and return
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        return self.construct(candidates, target, 0, 0, [], [])
        
    def construct(self, candidates, target, total, pos, curr, ret):
        
        if total > target:
            return ret
        if total == target:
            ret.append(curr)
            return ret
        for i in range(pos, len(candidates)):
            value = candidates[i]
            nex = curr + [value]
            total += value
            self.construct(candidates, target, total, i, nex, ret)
            total -= value
        return ret   
