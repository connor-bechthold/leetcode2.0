#My solution, ideal solution
#O(2^n) time, O(n) space (n is the length of the string)
class Solution:
    
    #Strategy: Straightforward backtrack, at each step we check:
    #If the current pos is an integer, go to the next char as we don't need to do anything
    #If the current pos is a letter, recursively call the function twice, one for the string with the current char as uppercase, and one for lowercase
    #Once we reach the last char, add the entire string to the output string list
    
    def letterCasePermutation(self, s: str) -> List[str]:
        return self.construct(s, 0, [])
        
    def construct(self, s, pos, strings):
        if pos == len(s) - 1:
            if not s[pos].isdigit():
                strings.append(s[:pos] + s[pos].upper())
                strings.append(s[:pos] + s[pos].lower())
            else:
                strings.append(s)

        elif s[pos].isdigit():
            self.construct(s, pos + 1, strings)
            
        else:
            self.construct(s[:pos] + s[pos].upper() + s[(pos + 1):], pos + 1, strings)
            self.construct(s[:pos] + s[pos].lower() + s[(pos + 1):], pos + 1, strings)
            
        return strings
