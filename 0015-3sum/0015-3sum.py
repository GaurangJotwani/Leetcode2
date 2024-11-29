class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        i = 0
        while i < len(nums) - 2:
            cNum = nums[i]
            l = i + 1
            r = len(nums) - 1
            while r > l:
                cSum = cNum + nums[r] + nums[l]
                
                if  cSum == 0:
                    res.append([cNum, nums[r], nums[l]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    r -= 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif cSum < 0:
                    l += 1
                else:
                    r -= 1
            i += 1
            while i < len(nums) - 2 and nums[i] == cNum:
                i += 1
        
        return res
        
            

