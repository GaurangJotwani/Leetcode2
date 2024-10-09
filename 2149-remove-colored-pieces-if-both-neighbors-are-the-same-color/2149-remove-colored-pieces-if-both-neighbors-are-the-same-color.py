class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        alice_moves = sum(1 for i in range(1, len(colors) - 1) if colors[i] == 'A' and colors[i - 1] == 'A' and colors[i + 1] == 'A')
        bob_moves = sum(1 for i in range(1, len(colors) - 1) if colors[i] == 'B' and colors[i - 1] == 'B' and colors[i + 1] == 'B')
        return alice_moves > bob_moves  # Alice wins if she has more moves than Bob