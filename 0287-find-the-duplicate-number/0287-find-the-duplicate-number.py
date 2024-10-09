class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums) - 1
        duplicate = 0

        # Iterate over each bit position up to log(n) bits
        for bit in range(n.bit_length()):  # Consider bits up to max number in range [1, n]
            base_count = 0
            nums_count = 0

            # Count bits in range [1, n] (base count)
            for num in range(1, n + 1):
                if num & (1 << bit):
                    base_count += 1

            # Count bits in the actual nums array (nums count)
            for num in nums:
                if num & (1 << bit):
                    nums_count += 1

            # If the actual array has more 1's in this bit position, set this bit in duplicate
            if nums_count > base_count:
                duplicate |= (1 << bit)

        return duplicate


        