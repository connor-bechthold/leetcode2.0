#My solution, ideal solution
#O(amount * n) time, where n in the length of the amount of coins
#O(amount) space
class Solution:
    #Strategy: Bottom up tabulation
    #Initialize a dp list of length amount + 1 (so the index corresponds to the change amount)
    #Initialize the first entry to be zero, as there's no coins that can make 0 cents
    #Initialize the rest of the values to amount + 1, as that's 1 more than the max amount of coins we can make for amount (all 1 cents)
    #Starting from an amount of 1, we find the min amount of coins we need to make that value
    #If that amount is in coins, the min value is 1, and we move forwards
    #Else, go through coins and subtract from amount values in coins that are less than amount. Since we've already determined min coins for those amounts, the min coins for the current amount may be that amount plus 1
    #We continue to do this, always updating the min until we reach the end
    #If we reach past amount and the value there is still amount + 1, no combination was found, and we return -1. Else we return the min amount
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        
        for i in range(1, amount + 1):
            if i in coins:
                dp[i] = 1
            else:
                for coin in coins:
                    if coin < i:
                        dp[i] = min(dp[i], dp[i - coin] + 1)
        return -1 if dp[amount] == amount + 1 else dp[amount]
