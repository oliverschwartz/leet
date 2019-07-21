class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        orig = []
        count = 0
        deck = sorted(deck)
        for i in range(n):
            if count >= 2:
                orig.append(orig[0])
                del orig[0]
            orig.append(deck[n - i - 1])
            count += 1
        orig.reverse()
        return orig
                