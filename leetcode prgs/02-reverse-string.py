class Solution:
    def reverseString(self, s: list[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

# Local Test Cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1: Standard input
    s1 = ["h", "e", "l", "l", "o"]
    sol.reverseString(s1)
    print("Test Case 1 Output:", s1)  # Expected: ['o', 'l', 'l', 'e', 'h']
    
    # Test Case 2: Edge case (Single element array)
    s2 = ["A"]
    sol.reverseString(s2)
    print("Test Case 2 Output:", s2)  # Expected: ['A']