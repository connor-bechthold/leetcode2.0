#My solution, ideal solution
#O(k * C(n, k)) time, O(k) space
class Solution: 
    #Strategy: Loop through the numbers 1 through n, adding them to our current combination until we reach a length of k, where we can add the combination to the return list
    #The trick here is as soon as we add a number to our combination, the following numbers have to be greater than the number we just added
    #If we don't check this, then we get duplicates and invalid combination
    #For ex. N = 4, K = 3
    #[1], [1,2], [1,2,3] (add), [1,2,4] (add), [1,3,4] (add)
    #You can see that for each subsequent value, we always start iterating at the value that's one more than the current
    #To implement this, we keep track of a pos variable, and increment it at each iteration
    def combine(self, n: int, k: int) -> List[List[int]]:
        return self.construct(n, k, 1, [], [])
    
    def construct(self, n, k, pos, curr, ret):
        if len(curr) == k:
            ret.append(curr)     
        else:
            for i in range(pos, n + 1):
                nex = curr + [i]
                self.construct(n, k, i + 1, nex, ret)
        return ret
