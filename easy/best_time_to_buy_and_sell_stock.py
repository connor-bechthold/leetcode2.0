#My solution, ideal solution
#O(n) time, O(1) space
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #Keep track of our max profit, and the current lowest price we can buy the stock for, looping through each day
        #If the current day price is less than the lowest price to buy we've seen, update it, as we may be able to make more profit later
        #If it's not, then we may make some sort of profit. Calculate this profit, and keep track of the max profit we've made, updating as necessary
        
        if len(prices) == 1:
            return 0
        
        max_profit = 0
        lowest_buy = prices[0]
        
        for i in range(1, len(prices)):
            if prices[i] < lowest_buy:
                lowest_buy = prices[i]
            else:
                current_profit = prices[i] - lowest_buy
                if current_profit > max_profit:
                    max_profit = current_profit
                    
        return max_profit
