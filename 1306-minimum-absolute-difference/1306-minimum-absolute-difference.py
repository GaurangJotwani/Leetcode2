class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        
        arr.sort()
        output = []
        minDiff = float("inf")

        for i in range(len(arr) - 1):
            d = abs(arr[i + 1] - arr[i])
            if d < minDiff:
                output = [[arr[i], arr[i + 1]]]
                minDiff = d
            elif d == minDiff:
                output.append([arr[i], arr[i + 1]])
        
        return output
