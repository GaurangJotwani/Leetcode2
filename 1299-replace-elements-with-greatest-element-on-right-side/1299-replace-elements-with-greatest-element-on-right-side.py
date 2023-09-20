class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        if len(arr) == 1: return [-1]
        
        greatest_seen = arr[-1]
        
        for i in range(len(arr) - 2, -1, -1):
            temp = greatest_seen
            greatest_seen = max(greatest_seen, arr[i])
            arr[i] = temp
            
        
        arr[-1] = -1
        return arr
        