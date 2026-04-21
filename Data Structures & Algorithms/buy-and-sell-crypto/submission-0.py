class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Brute for way of doing this
        n = len(prices)
        max_prof = 0
        for i, price in enumerate(prices):
            print(price)
            j = i +1
            while j< n:
                max_prof = max(max_prof, prices[j] - price)
                j += 1
            
        return max_prof
