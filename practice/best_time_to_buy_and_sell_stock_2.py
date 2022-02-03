class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        # Buying/selling based on peaks/valleys is the SAME as buying sellign whenever there is a small increase. Therefore we can try a greedy algorithm
        
        profit = 0
        buy=0
        for i in range(0,len(prices)-1,1):
            if prices[i+1] and prices[i+1]>prices[i]:
                profit+=prices[i+1]-prices[i]
                
        return profit
            
        