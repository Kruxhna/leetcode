"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None :
            return None

        curr = head
        while curr :
            dNode = Node(curr.val)
            dNode.next = curr.next
            curr.next = dNode
            curr = dNode.next

        curr = head
        while curr :
            if curr.random :
                curr.next.random = curr.random.next
            curr = curr.next.next

        curr = head
        chead = head.next
        ccurr = chead

        while ccurr.next :
            curr.next = curr.next.next
            ccurr.next = ccurr.next.next

            curr = curr.next
            ccurr = ccurr.next

        curr.next = ccurr.next = None

        return chead