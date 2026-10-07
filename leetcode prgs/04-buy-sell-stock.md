## Problem: Best Time to Buy and Sell Stock (Easy)
**Link:** https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

### Approach
Used a single-pass greedy approach keeping track of the minimum buy price seen so far and continuously updating the maximum potential profit.

### Complexity
- Time: $O(n)$
- Space: $O(1)$

### Notes
Avoids $O(n^2)$ brute-force comparisons by updating profit dynamically in a single iteration.