class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1
        for char in t:
            if char not in count or count[char] == 0:
                return False
            count[char] -= 1
        return True

# Local Test Cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1: Valid anagram
    print("Test Case 1 Output:", sol.isAnagram("anagram", "nagaram"))  # Expected: True
    
    # Test Case 2: Edge case (Different lengths)
    print("Test Case 2 Output:", sol.isAnagram("rat", "car"))          # Expected: False