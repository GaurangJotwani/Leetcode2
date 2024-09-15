from collections import deque
from itertools import accumulate, chain
from math import inf

MAX = 10 ** 9 + 7


class Solution:
    def maxSumMinProduct(self, A: list[int]) -> int:
        """
        @also see https://leetcode.com/problems/maximum-subarray-min-product/solutions/1198800/python3-mono-stack/
        :param A: 
        :return: 
        """
        # prefix_sum[i] = sum(A[:i])
        prefix_sum = [*accumulate(A, initial=0)]

        # creating monotonic increasing stack
        push, pop = (stk := deque()).append, stk.pop

        output = 0

        for i, a in enumerate(chain(A, [-inf])):
            while stk and A[stk[-1]] >= a:
                mn = A[pop()]

                j = stk[-1] if stk else -1

                output = max(
                    output,
                    mn * (prefix_sum[i] - prefix_sum[j + 1])  # mn * sum(A[j: i])
                )

            push(i)

        return output % MAX