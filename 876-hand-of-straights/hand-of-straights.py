import collections
import heapq
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize != 0 :
            return False

        card_c = collections.Counter(hand)
        min_heap = list(card_c.keys())
        heapq.heapify(min_heap)

        while min_heap :

            small = min_heap[0]
            if card_c[small] == 0 :
                heapq.heappop(min_heap)
                continue

            for i in range(groupSize) :
                curr = small + i
                if card_c[curr] == 0 :
                    return False
                card_c[curr] -= 1
        return True