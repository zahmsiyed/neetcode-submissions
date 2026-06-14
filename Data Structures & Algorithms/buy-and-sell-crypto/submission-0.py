class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_gain = 0
        for i in range(0,len(prices)-1):
            for j in range(i+1,len(prices)):
                diff = prices[j]-prices[i]
                if diff>max_gain: 
                    max_gain=diff
        return max_gain
