#My solution, ideal solution
#O(n^2) time, O(1) space
class Solution:
    
    #Strategy: Expand around each letter to check for a palindrome, starting at the first letter
    #This is because palindromes can be even or odd. If they're even, there's no middle, so our start and end pointer must be different
    #So, for each letter, we call it twice - one for even (starting at the current letter and the letter before i) and one for odd (both at the same letter)
    #We simply expand the pointers outwards, and stop once we each the start/end or the letters at the pointers don't equal each other
    #We keep a global "greatest" variable that is updated as we go with the longest palindrome
    
    greatest = ""
    
    def longestPalindrome(self, s: str) -> str:
        
        self.greatest = s[0]
        for i in range(1, len(s)):
            self.extendPalindrome(i - 1, i, s) 
            self.extendPalindrome(i,i, s)
                  
        return self.greatest
                
    def extendPalindrome(self, front, back, s):
            while front >= 0 and back < len(s) and s[front] == s[back]:
                front -= 1
                back += 1
            substring = s[front+1:back]
            if len(self.greatest) < len(substring):
                self.greatest = substring
