class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:

        total = sum(nums)
        if total % k != 0:
            return False

        target = total // k
        nums.sort(reverse=True)  # Sort in descending order to place larger numbers first

        if nums[0] > target:  # Early exit if the largest number is greater than the target sum
            return False
        
        used = [False] * len(nums)  # Boolean array to mark elements as used

        def backtrack(index, current_sum, groups_formed):
            if groups_formed == k - 1:  # If we've formed k - 1 groups, the last group will automatically be correct
                return True
            
            if current_sum == target:  # If current subset matches the target, start a new group
                return backtrack(0, 0, groups_formed + 1)
            
            for i in range(index, len(nums)):
                if used[i] or current_sum + nums[i] > target:  # Skip if already used or exceeds target
                    continue
                
                # Mark as used and try adding this number to the current group
                used[i] = True
                if backtrack(i + 1, current_sum + nums[i], groups_formed):
                    return True
                used[i] = False  # Backtrack and unmark this element
            
                # Early termination: if we can't start a group with nums[i], no point in continuing
                if current_sum == 0:
                    break
            
            return False

        return backtrack(0, 0, 0)

