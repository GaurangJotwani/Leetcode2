class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        
        c, num = ord(coordinates[0]) - ord('a') + 1, int(coordinates[1])
        print(c, num, c + num)

        return False if (c + num) % 2 == 0 else True
