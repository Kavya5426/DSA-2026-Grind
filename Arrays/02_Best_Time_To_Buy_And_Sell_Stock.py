"""
Problem: Best Time to Buy and Sell Stock
Platform: LeetCode
Difficulty: Easy
Date: 24-02-2026

Approach:
- Keep track of the minimum price seen so far.
- For each day, calculate the potential profit by subtracting the minimum price from current price.
- Update maximum profit if the current profit is greater.
- If a new lower price is found, update the minimum price.
- This ensures we buy at the lowest price before selling.

Time Complexity: O(n)
Space Complexity: O(1)
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price=prices[0]
        max_profit=0
        for i in range(1,len(prices)):
            if prices[i]<min_price:
                min_price=prices[i]
            else:
                max_profit=max(max_profit,prices[i]-min_price)
        return max_profit