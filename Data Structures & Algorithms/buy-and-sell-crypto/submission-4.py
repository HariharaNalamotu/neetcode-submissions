class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        left = 0
        right = 1
        maxp = 0
        while right < len(prices):
            if prices[right]-prices[left] > 0:
                if prices[right]-prices[left] > maxp:
                    maxp = prices[right]-prices[left]
            else:
                left = right
            right += 1
            
        return maxp
        