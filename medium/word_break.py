#My solution, ideal solution
#O(n^3) time, O(n) space
class Solution:
    #Strategy: The ith index of our dp list correlates to the i-1th letter within s. This means that the first index within dp is defaulted to True
    #If the index is true, it means that the substring ending at that letter can be formed from words within the word dictionary
    #To verify this, at each letter, we iterate from the first letter into s up until the letter right before the current letter
    #At each previous letter, we check in the dp list to see if the substring ending at that letter can be formed from words in wordDict
    #If it can, we also then check to see if the substring following that letter up to the current letter
    #If this also is true, then we know the current letter can be formed from words in wordDict, so we set that index to True
    #At the end, the value at the end of the dp list will contain the output of the algorithm
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        lookup = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(0, i):
                if dp[j] == True and s[j:i] in lookup:
                    dp[i] = True
        return dp[len(s)]
