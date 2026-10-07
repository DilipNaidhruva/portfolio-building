## Problem: Valid Anagram (Easy)
**Link:** https://leetcode.com/problems/valid-anagram/

### Approach
Used a hash map frequency counter to track character occurrences in the first string and decrement them while iterating through the second string.

### Complexity
- Time: $O(n)$
- Space: $O(1)$ (since character space is bounded by 26 English letters)

### Notes
Early exit check `len(s) != len(t)` handles unequal lengths immediately without extra iteration.