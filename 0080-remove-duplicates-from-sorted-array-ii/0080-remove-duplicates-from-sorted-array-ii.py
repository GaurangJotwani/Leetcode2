class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 0
    
        r = 0

        while r < len(nums):
            cNum = nums[r]
            print(idx, r, cNum)
            if r + 2 < len(nums) and nums[r + 2] == cNum:
                nums[idx] = cNum
                nums[idx + 1] = cNum
                idx += 2
                while r < len(nums) and nums[r] == cNum:
                    r += 1
                continue
            
            nums[idx] = cNum
            idx += 1
            r += 1
        return idx
    
