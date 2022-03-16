#My solution, ideal solution
#O(n^2) time, O(1) space
class Solution:
    #Strategy: Same as longest palindromic substring
    #Loop through string, and expand out around each letter (odd) and the letter before the current letter concatenated with the current letter
    #Everytime we have a valid palindrome, increment the count
    def countSubstrings(self, s: str) -> int:
        
        sol = 1
        for i in range(1, len(s)):
            sol += self.isPal(s, i - 1, i) + self.isPal(s, i, i)              
        return sol
        
    def isPal(self, s, front, back):
        
        validPals = 0
        while front >= 0 and back < len(s) and s[front] == s[back]:
            validPals += 1
            front -= 1
            back += 1
        
        return validPals
