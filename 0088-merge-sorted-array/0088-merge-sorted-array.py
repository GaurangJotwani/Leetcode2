class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = len(nums1) - 1
        m -= 1
        n -= 1
        while m >= 0 or n >= 0:
            num1 = nums1[m] if m >= 0 else float("-inf")
            num2 = nums2[n] if n >= 0 else float("-inf")
            if num1 > num2:
                nums1[i] = num1
                m -= 1
            else:
                nums1[i] = num2
                n -= 1
            i -= 1
