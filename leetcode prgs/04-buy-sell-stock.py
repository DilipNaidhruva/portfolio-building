class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        return max_profit

# Local Test Cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1: Standard input
    print("Test Case 1 Output:", sol.maxProfit([7, 1, 5, 3, 6, 4]))  # Expected: 5
    
    # Test Case 2: Edge case (Monotonically decreasing prices -> 0 profit)
    print("Test Case 2 Output:", sol.maxProfit([7, 6, 4, 3, 1]))     # Expected: 0