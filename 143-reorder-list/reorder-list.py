# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None :
            return None

        slow = fast = head
        while fast and fast.next :
            slow = slow.next
            fast = fast.next.next

        curr = slow.next
        slow.next = None
        prev = None
        while curr :
            nxtNode = curr.next
            curr.next = prev
            prev = curr
            curr =nxtNode

        head2 = prev

        while head2 :
            temp1, temp2 = head.next, head2.next
            
            head.next = head2
            head2.next = temp1

            head = temp1
            head2 = temp2
