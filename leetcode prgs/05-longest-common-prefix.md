## Problem: Longest Common Prefix (Easy)
**Link:** https://leetcode.com/problems/longest-common-prefix/

### Approach
Used horizontal scanning starting with the first string as the prefix candidate and trimming characters off the end until matching each subsequent string.

### Complexity
- Time: $O(S)$ where $S$ is the sum of all characters in all strings
- Space: $O(1)$

### Notes
Trimming the prefix dynamically handles early exit scenarios when no prefix is shared (`prefix` becomes empty).