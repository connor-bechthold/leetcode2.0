#My solution, ideal solution
#Thus, time complexity is O(k * len(candi)^k)
#Space complexity is O(target / min(candidate)) (or O(k))
class Solution:
    
    #Strategy: Since there are duplicate elements, we first sort the array
    #At every element, instead of calling the function again with the pos index starting at that index, we increase it by one, as we can't use each element more than once
    #To check for duplicates, we check if the current index is greater than the index that the function was called with (for ex. [1,1,2] 2, we still want to add [1,1] as a possible combination)
    #We also check if the current value at the current index is the same as the previous value
    #If it is, we can skip it, as we've already seen it
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        return self.construct(candidates, target, 0, 0, [], [])
        
    def construct(self, candidates, target, total, pos, curr, ret):
        print(curr)
        if total > target:
            return ret
        if total == target:
            ret.append(curr)
            return ret
        for i in range(pos, len(candidates)):
            if i > pos and candidates[i] == candidates[i - 1]:
                continue
            value = candidates[i]
            nex = curr + [value]
            total += value
            self.construct(candidates, target, total, i + 1, nex, ret)
            total -= value
        return ret
