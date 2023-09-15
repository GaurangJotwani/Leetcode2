class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        if len(nums) == 1:
            return nums
        l1 = self.sortArray(nums[:len(nums)//2])
        l2 = self.sortArray(nums[len(nums)//2:])
        
        ptr_1, ptr_2 = 0, 0
        merged_l = []
        while ptr_1 < len(l1) and ptr_2 < len(l2):
            if l1[ptr_1] < l2[ptr_2]:
                merged_l.append(l1[ptr_1])
                ptr_1 += 1
            else:
                merged_l.append(l2[ptr_2])
                ptr_2 += 1
        
        if ptr_1 != len(l1):
            while ptr_1 < len(l1):
                merged_l.append(l1[ptr_1])
                ptr_1 += 1
        elif ptr_2 != len(l2):
            while ptr_2 < len(l2):
                merged_l.append(l2[ptr_2])
                ptr_2 += 1
        
        
        return merged_l
            
        
        
            
            
        