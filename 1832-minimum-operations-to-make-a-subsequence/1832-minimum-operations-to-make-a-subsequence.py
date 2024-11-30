class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        
        index_map = {num:i for i,num in enumerate(target)}
        arr2 = [index_map[num] for num in arr if num in index_map]

        #LIS
        sub = []
        for num in arr2:
            idx = bisect_left(sub, num)
            if idx >= len(sub):
                sub.append(num)
            else:
                sub[idx] = num
        
        return len(target) - len(sub)
    
    def binary_search(self,arr,num):
        l,r = 0, len(arr) - 1
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] > num:
                r = mid - 1
            else:
                l = mid + 1
        return l



        