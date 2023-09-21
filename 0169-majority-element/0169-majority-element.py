class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        nums.sort()

        i = 0
        majority = ceil(len(nums) / 2)
        print(majority)

        while i < len(nums):

            c_num = nums[i]
            c_freq = 1
            i += 1
            while i < len(nums) and nums[i] == c_num:
                i += 1
                c_freq += 1
                if c_freq >= majority:
                    return c_num
        
        return 0
             
        