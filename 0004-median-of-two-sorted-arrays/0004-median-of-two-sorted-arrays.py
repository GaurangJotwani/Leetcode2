class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        total = len(nums1) + len(nums2)
        left_size = total // 2

        l, r = 0, len(nums1) - 1

        while True:
            mid1 = (l + r) // 2
            mid2 = left_size - (mid1 + 1) - 1

            left_num1 = nums1[mid1] if mid1 >= 0 else float("-inf")
            right_num1 = nums1[mid1 + 1] if mid1 + 1 < len(nums1) else float("inf")
            left_num2 = nums2[mid2] if mid2 >= 0 else float("-inf")
            right_num2 = nums2[mid2 + 1] if mid2 + 1 < len(nums2) else float("inf")

            # Check if we found the correct partition
            if left_num1 <= right_num2 and left_num2 <= right_num1:
                if total % 2 == 0:
                    return (max(left_num1, left_num2) + min(right_num1, right_num2)) / 2
                else:
                    return min(right_num1, right_num2)

            # Adjust search range
            if left_num1 > right_num2:
                r = mid1 - 1
            else:
                l = mid1 + 1
