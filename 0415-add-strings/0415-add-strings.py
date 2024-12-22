class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        carry = 0
        i = len(num1) - 1
        j = len(num2) - 1

        res = []

        while i >= 0 or j >= 0 or carry > 0:
            temp_num1 = int(num1[i]) if i >= 0 else 0
            temp_num2 = int(num2[j]) if j >= 0 else 0

            tmp_sum = temp_num1 + temp_num2 + carry
            carry = tmp_sum // 10
            res.append(str(tmp_sum % 10))
            i -= 1
            j -= 1
        
        res.reverse()
        return "".join(res)