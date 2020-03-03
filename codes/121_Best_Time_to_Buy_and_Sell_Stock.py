# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
# 121. Best Time to Buy and Sell Stock
# Easy
#
# 4036
#
# 183
#
# Add to List
#
# Share
#
# Say you have an array for which the ith element is the price of a given stock on day i.

# If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
# Note that you cannot sell a stock before you buy one.

# Example 1:

# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#              Not 7-1 = 6, as selling price needs to be larger than buying price.
# Example 2:

# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.

# %%


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n <= 1:
            return 0
        profit = 0
        curr_low = prices[0]
        for i in range(1, n):
            curr_price = prices[i]
            if curr_price <= curr_low:
                curr_low = curr_price
            else:
                profit = max(curr_price - curr_low, profit)

        return profit


# %%
prices = [7, 6, 4, 3, 1]
Solution().maxProfit(prices)

prices = [7, 1, 5, 3, 6, 4]
Solution().maxProfit(prices)

# %%


class SolutionV1:
    def maxProfit(self, prices):
        if prices == []:
            return 0
        iMin = 0
        iMax = iMin
        profit = 0
        minP = prices[iMin]
        maxP = minP

        while iMin < len(prices):
            while iMax < len(prices):
                if prices[iMax] < minP:
                    iMin, minP, maxP = iMax, prices[iMax], prices[iMax]
                elif prices[iMax] > maxP:
                    maxP = prices[iMax]
                    newProfit = maxP - minP
                    if newProfit > profit:
                        profit = newProfit
                iMax += 1
            iMin += 1

        return profit


class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        if n == 0 or n == 1:
            return 0
        profit = 0
        maxP = prices[-1]
        for i in range(n - 2, -1, -1):
            maxP = max(maxP, prices[i])
            if maxP - prices[i] > profit:
                profit = maxP - prices[i]
        return profit


prices = [7, 1, 5, 3, 6, 4]
# prices = [7, 6, 4, 3, 1]
Solution().maxProfit(prices)

len(prices)

Solution().maxProfit([])
len([])
