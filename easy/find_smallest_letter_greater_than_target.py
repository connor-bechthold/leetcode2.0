#My solution, ideal solution
#O(log(n)) time, O(1) space
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        #Strategy: Simply a modified binary search. Instead of returning the index of the found item, we will always return the index of the next greatest letter after the target letter, which will always be located at start
        #Since wrap around is possible, we check for that at the end, and return the first letter in the list if true
        start = mid = 0
        end = len(letters) - 1
        
        while start <= end:
            mid = (start + end) // 2
            if letters[mid] <= target:
                start = mid + 1
            else:
                end = mid - 1
         
        if start == len(letters):
            return letters[0]
        else:
            return letters[start]
