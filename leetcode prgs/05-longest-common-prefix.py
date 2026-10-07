class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        
        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
                    
        return prefix

# Local Test Cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1: Standard input
    print("Test Case 1 Output:", sol.longestCommonPrefix(["flower", "flow", "flight"]))  # Expected: 'fl'
    
    # Test Case 2: Edge case (No common prefix)
    print("Test Case 2 Output:", sol.longestCommonPrefix(["dog", "racecar", "car"]))     # Expected: ''