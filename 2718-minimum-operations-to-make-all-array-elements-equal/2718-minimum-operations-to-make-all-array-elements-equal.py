from typing import List

class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        # Sort the array
        nums.sort()
        n = len(nums)
        
        # Calculate prefix sums
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        
        result = []
        for q in queries:
            # Use binary search to find the position where q would fit in the sorted array
            pos = bisect.bisect_left(nums, q)
            
            # Calculate operations needed to make all elements equal to q
            left_ops = q * pos - prefix_sum[pos]  # Operations for elements less than q
            right_ops = (prefix_sum[-1] - prefix_sum[pos]) - q * (n - pos)  # Operations for elements greater than q
            result.append(left_ops + right_ops)

        return result

# Approach: Sort `nums`, calculate position and prefix sum manually, and compute operations for each query.
# Time Complexity: O((n + m) * n)
# Space Complexity: O(n), where n is the length of `nums` and m is the length of `queries`.
