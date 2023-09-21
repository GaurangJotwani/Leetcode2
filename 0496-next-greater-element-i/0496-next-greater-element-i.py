class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        indices = {}
        pre_tab = [-1] * len(nums2)
        print(pre_tab)

        for idx, num in enumerate(nums2):
            indices[num] = idx

            for j in range(idx + 1, len(nums2)):
                if nums2[j] > num:
                    pre_tab[idx] = nums2[j]
                    break
        output = []
        for num in nums1:
            output.append(pre_tab[indices[num]])
        
        return output
        