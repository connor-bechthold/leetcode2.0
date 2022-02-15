#My solution, ideal solution
#O(n * 2^n) time (there are 2^n subsets, and for each subset, we must go through a for loop at most n times)
#O(n) space for the curr array, also depth of recursion tree is n

class Solution:
    #Strategy: DFS backtracking approach
    #We keep track of a curr path and everytime we enter the construct function, we add this path to the solution array
    #At each instance, we add each following element to our current path and individually call the function again each time, incrementing the pos integer so we are always looking at the next element ahead each time
    #To visulaize this, take [1,2]
    #[[], [1], [1, 2], [2]]
    #We start with an empty array and first iterate through each following element
    #We first add 1, then the function is called with 1 within the current path while also updating pos. So, the first element now is 2, which means we add [1, 2], and increment pos
    #Pos now equals 2, the length of nums, so we backtrack all the way to the empty curr list, i is incremented, and we add 2, and return sol, the list above
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.construct(nums, 0, [], [])
        
    def construct(self, nums, pos, curr, sol):
        sol.append(curr)
        for i in range(pos, len(nums)):
            self.construct(nums, i + 1, curr + [nums[i]], sol)
        return sol
