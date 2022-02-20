#My solution, ideal solution
#O(2^2n ) time (we make 2 decisions at each node, so there will be 2^n leaf nodes, however, we have to do this for each closing and open bracket, so 2^2n)
#O(n) space (actually 2n in depth, which simplifies to n)
class Solution:
    
    #Strategy: Simple backtracking, keep adding open brackets until we can't, then add closing brackets until we can't
    #Once we find a solution, backtrack and add a closing bracket instead of an open bracket, and continue the same process
    #Along the way, keep track of the number of closing and open brackets we've used, and also our current combination
    #Once we verify we have a valid combination, add it to the output list, and continue
    def generateParenthesis(self, n: int) -> List[str]:
        return self.construct(n, 0, 0, "", [])
        
    def construct(self, n, op, cl, curr, ret):
        
        if op == n and cl == n:
            ret.append(curr)
            return ret

        if op < n:
            self.construct(n, op + 1, cl, curr + "(", ret)

        if cl < op:
            self.construct(n, op, cl + 1, curr + ")", ret)

        return ret
