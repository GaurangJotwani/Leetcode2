class Solution:
    def isStrobogrammatic(self, num: str) -> bool:

        l = 0
        r = len(num) - 1
        while l <= r:
            if l == r:
                if num[l] not in ["0", "8", "1"]:
                    return False
                else:
                    return True
            if (num[l] == "6" and num[r] == "9") or (num[r] == "6" and num[l] == "9"):
                l += 1
                r -= 1
                continue
            if num[l] == num[r] and num[l] in ["0", "8", "1"]:
                l += 1
                r -= 1
            else:
                return False
        return True
            
        