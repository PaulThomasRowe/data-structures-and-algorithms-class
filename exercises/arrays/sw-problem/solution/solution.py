class Solution:
    def maxProfit(self, prices):
        print(f"The provided prices are {prices}")
        left = 0 #Buy
        print(f"The initial left value is {left}")
        right = 1 #Sell
        print(f"The initial right value is {right}")
        max_profit = 0
        print(f"The initial max profit is {max_profit}")
        while right < len(prices):
            print(f"The current right value is {right}.")
            currentProfit = prices[right] - prices[left] #our current Profit
            print(f"Current profit is {prices[right]}(index:{right}) - {prices[left]}(index:{left}) = {currentProfit}")
            if prices[left] < prices[right]:
                max_profit = max(currentProfit, max_profit)
                print(f"New max profit is {max_profit}")
            else:
                left = right
                print(f"Left goes from {left} to {right}")
            right += 1
            print(f"Right is now {right}")
        print(f"Max profit is {max_profit}")
        return max_profit
