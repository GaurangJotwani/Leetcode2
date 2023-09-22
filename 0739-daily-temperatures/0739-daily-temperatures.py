class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            c_temp = temperatures[i]
            while stack and stack[-1][0] < c_temp:
                temp, idx = stack.pop()
                res[idx] = i - idx
            
            stack.append([c_temp, i])
        
        return res

        