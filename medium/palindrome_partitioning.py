#My solution, ideal solution
#O(n * 2^n) time - palindrome is O(n), and each iteration has 2 choices:
# - Substring is not a palindrome, add onto it
# - Substring is a palindrome, call the function again and initialize a new substring
#Thus, worst case, we have 2^N substrings
#O(n) space - depth of recursion tree
class Solution:
    
    #Strategy: Backtracking approach, keep track of the current pos we're at, as well as our current combination and the return list
    #At each position, we keep track of a substring starting at that position and ending at the end of the string
    #Every iteration, we add onto this string
    #If the string is ever a palindrome, we add it to our current combination, and call the function again with the the updated array, starting at the position after the last letter in the substring
    #Once our position var is at the length of the string, we've found a new palindrome partition and can add it to the return array
    def partition(self, s: str) -> List[List[str]]:
        return self.construct(s, 0, [], [])
        
    def construct(self, s, pos, curr, ret):
        if pos == len(s):
            ret.append(curr)
        else:
            word = ""
            for i in range(pos, len(s)):
                word += s[i]
                if self.isPalindrome(word):
                    self.construct(s, i + 1, curr + [word], ret)
        return ret
                
        
    def isPalindrome(self, s):
        l = 0 
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
