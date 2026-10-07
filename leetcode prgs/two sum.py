class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i
        return []

# Local Test Cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1: Standard input
    print("Test Case 1 Output:", sol.twoSum([2, 7, 11, 15], 9))  # Expected: [0, 1]
    
    # Test Case 2: Edge case (Negative numbers and duplicate values)
    print("Test Case 2 Output:", sol.twoSum([-3, 4, 3, 90], 0))   # Expected: [0, 2]
