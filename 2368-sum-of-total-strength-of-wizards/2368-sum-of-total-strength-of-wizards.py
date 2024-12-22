class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        mod,n = 10 ** 9 + 7, len(strength)

        right_index = [n] * n
        stack = []

        for i in range(n):
            while stack and strength[stack[-1]] >= strength[i]:
                right_index[stack.pop()] = i
            stack.append(i)
        left_index = [-1] * n
        stack = []

        for i in range(n - 1, -1, -1):
            while stack and strength[stack[-1]] > strength[i]:
                left_index[stack.pop()] = i
            stack.append(i)
        

        presum_of_presum = list(accumulate(accumulate(strength, initial=0),initial=0))

        answer = 0

        for i in range(n):
            left_bound = left_index[i]
            right_bound = right_index[i]

            left_count = i - left_bound
            right_count = right_bound - i

            neg_presum = (presum_of_presum[i + 1] - presum_of_presum[i - left_count + 1]) % mod
            pos_presum = (presum_of_presum[i + right_count + 1] - presum_of_presum[i + 1]) % mod

            answer += strength[i] * (pos_presum * left_count - neg_presum * right_count)
            answer %= mod
        
        return answer

