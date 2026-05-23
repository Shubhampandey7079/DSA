class Solution:
    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
        prefixes = set()
        
        # Step 1: Build the pool of all valid prefixes from arr1
        for val in arr1:
            while val > 0:
                prefixes.add(val)
                val //= 10  # Strip the last digit to get the next prefix
                
        longest_prefix_length = 0
        
        # Step 2: Check prefixes of elements in arr2 against the set
        for val in arr2:
            while val > 0:
                if val in prefixes:
                    # Length of an integer can be found by converting to string
                    longest_prefix_length = max(longest_prefix_length, len(str(val)))
                    break  # Optimization: shorter prefixes of this number won't beat the current match
                val //= 10
                
        return longest_prefix_length