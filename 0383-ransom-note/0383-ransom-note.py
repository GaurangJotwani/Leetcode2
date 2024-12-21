class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter_ransom = Counter(ransomNote)
        counter_magazine = Counter(magazine)

        for char,freq in counter_ransom.items():
            if char not in counter_magazine or freq > counter_magazine[char]:
                return False
        
        return True
