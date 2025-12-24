import heapq
class Solution:
    def isPossible(self, target: List[int]) -> bool:
        if len(target) == 1 :
            return target[0] == 1

        total_sum = sum(target)
        max_heap = [-x for x in target]
        heapq.heapify(max_heap)

        while -max_heap[0] > 1 :
            max_val = -heapq.heappop(max_heap)
            rest_sum = total_sum - max_val

            if rest_sum == 1 :
                return True
            if rest_sum == 0 or max_val <= rest_sum :
                return False

            prev_val = max_val%rest_sum 

            if prev_val == 0 :
                return False

            total_sum = rest_sum + prev_val
            heapq.heappush(max_heap,-prev_val)
        return True