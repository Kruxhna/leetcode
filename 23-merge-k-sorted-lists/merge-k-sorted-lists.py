# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        counter = 0

        for lhead in lists :
            if lhead :
                heapq.heappush(min_heap,(lhead.val,counter,lhead))
                counter += 1

        dummy = ListNode(-1)
        tail = dummy

        while min_heap :
            val, _ , node = heapq.heappop(min_heap)

            tail.next = node
            tail = tail.next

            if node.next :
                heapq.heappush(min_heap, (node.next.val, counter, node.next))
                counter += 1
        return dummy.next        