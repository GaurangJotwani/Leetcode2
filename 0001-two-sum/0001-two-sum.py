class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = [-1, -1]

        seen = {}

        for i, num in enumerate(nums):
            difference = target - num
            if difference in seen:
                answer[0] = i
                answer[1] = seen[difference]
                return answer
            seen[num] = i
        
        