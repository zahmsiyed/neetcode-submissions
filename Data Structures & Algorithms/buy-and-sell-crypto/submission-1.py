class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        for i in range(len(prices)):
            sell = prices[i]
            buys = prices[:i]
            for buy in buys:
                best = max(best, sell-buy)
        
        if best < 0:
            return 0
        return best

        