#My solution, ideal solution
#O(4^n) time (for ex, someone types in "999999999", then each node in the recursion tree, besides the leaf nodes will have 4 children each)
#O(n) space (n is the length of digits)
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #Strategy: Backtracking approach, keep track of a lookup table of the digits mapped to strings
        #Within our recursive function, keep track of the current string combination we have, and the position in the digit string we're at
        #If our current combination is the length of the digit string, we have a valid combination, and add it to the return array
        #Else, grab the current string of letters from the lookup table (depending on the current position)
        #For each letter, add it to the current string, and call the function with the updated string, incrementing to the next position
        #We have a separate case for an empty string, else the algorithm will return [""] and not []
        lookup = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        ret = []
        
        def construct(curr, pos):
            
            if (len(curr) == len(digits)):
                ret.append(curr)
            else:
                letters = lookup[digits[pos]]
                for l in letters:
                    construct(curr + l, pos + 1)
        
        if not len(digits):
            return ret
        
        construct("", 0)
        return ret
