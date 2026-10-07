## Problem: Reverse String (Easy)
**Link:** https://leetcode.com/problems/reverse-string/

### Approach
Used a two-pointer technique (left and right) moving towards the center, swapping elements in-place to achieve $O(1)$ extra memory usage.

### Complexity
- Time: $O(n)$
- Space: $O(1)$

### Notes
Modifying the list in-place avoids allocating extra memory for a new list, satisfying the $O(1)$ auxiliary space constraint.