class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        min_seen = prices[0]
        for i in range(1,len(prices)):
            max_profit = max(max_profit, prices[i]-min_seen)
            if min_seen > prices[i]:
                min_seen = prices[i]
        return max_profit
