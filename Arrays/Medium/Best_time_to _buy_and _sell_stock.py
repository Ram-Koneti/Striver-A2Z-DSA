"""
Problem:
Best Time to Buy and Sell Stock

Source:
LeetCode

Link:
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Approach:
Track minimum price so far and calculate profit at each step.
Update maximum profit whenever a higher profit is found.

Time Complexity:
O(n)

Space Complexity:
O(1)

Pattern:
Greedy / One Pass
"""

def max_profit(prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        else:
            profit = price - min_price
            max_profit = max(max_profit, profit)

    return max_profit
