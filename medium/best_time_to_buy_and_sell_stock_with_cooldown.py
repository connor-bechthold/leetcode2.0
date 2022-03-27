#Ideal solution
#O(n) time, O(n) space
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #Strategy: State diagram with states HOLD, BUY, and SELL
        #At each index, our current results are based off the previous day
        #So at index i, our results are based off the stock price on day i and our results from day i - 1
        
        hold = [0] * len(prices)
        buy = [0] * len(prices)
        sell = [0] * len(prices)
    
        hold[0] = 0 #We have no possible profit to hold on the first day
        buy[0] = -prices[0] #Profit after after buying the first stock (negative, pain)
        sell[0] = 0 #We haven't bought anything the previous day, so we can't sell anything
    
        for i in range(1, len(prices)):
            #The max profit we can make at the hold state is either holding what we currently have profited from, or what we've profited from what we've sold the prev day
            hold[i] = max(hold[i - 1], sell[i - 1])
        
            #The max profit we can make at the buy state is either keeping whatever we've currently bought or subtracting what we can currently buy from the profit we've made
            #Again, we always want to keep buying what's going to lose us the least money, so that's why we take the max
            buy[i] = max(buy[i - 1], hold[i - 1] - prices[i])
        
            #There's only one thing we can do at the sell state - SELL! This will be whatever price we were currently at after buying the prev day plus the current stock price we will sell at
            sell[i] = buy[i - 1] + prices[i]
        
        #At the end, we need to check whether we made more by selling on the last day or holding
        return max(hold[len(prices) - 1], sell[len(prices) - 1])
        
#Optimized solution
#O(n) time, O(1) space
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #Same strategy, but we can optimize the space
        hold = 0
        buy = -prices[0]
        sell = 0
        
        for i in range(1, len(prices)):
            
            prevSell = sell
            sell = buy + prices[i]
            buy = max(buy, hold - prices[i])
            hold = max(hold, prevSell)
            
        return max(hold, sell)
