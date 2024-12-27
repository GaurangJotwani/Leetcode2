class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:

        
        n = len(arr)
        target = n / 4

        i = 0

        while i < n:
            num = arr[i]
            j = i

            while j < n and arr[j] == num:
                j += 1
            
            if j - i > target:
                return num
            
            i = j
            


        