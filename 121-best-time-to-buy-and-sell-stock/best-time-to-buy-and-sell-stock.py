class Solution:
    def maxProfit(self, prices):
        l,r,max_profit = 0,1,0

        while r < len(prices) :
            if prices[r] > prices[l] :
                profit = prices[r] - prices[l]

                max_profit = max(max_profit,profit)
            else :
                l = r
            r += 1
        return max_profit
            