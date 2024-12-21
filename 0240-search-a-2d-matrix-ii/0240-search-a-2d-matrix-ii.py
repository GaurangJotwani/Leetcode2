class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        s_r = len(matrix) - 1

        while s_r >= 0:
            if self.binarySearch(target, matrix[s_r]):
                return True
            s_r -= 1
        
        return False
        
    
    def binarySearch(self, target, lst):
        l,r = 0, len(lst) - 1
        while l <= r:
            mid = (l + r) // 2
            if lst[mid] == target:
                return True
            if lst[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False