# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def reverse(self, head):
        """Reverses a given linked list."""
        temp, prev = head, None

        # Loop until we reach the end of the list
        while temp: 
            nxtNode = temp.next
            temp.next = prev
            prev = temp
            temp = nxtNode
        return prev
    
    def getKTHnode(self, temp, k):
        """Finds the k-th node from the given 'temp' node."""
        k -= 1
        while temp and k > 0:
            k -= 1
            temp = temp.next
        return temp

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head
        prevl = None  # This will be the tail of the previous reversed group

        while temp:
            # 1. Find the k-th node of the current group
            knode = self.getKTHnode(temp, k)

            # 2. If no k-th node, we are at the end (less than k nodes left)
            if knode is None:
                # Link the previous group's tail to the remaining nodes
                if prevl:
                    prevl.next = temp
                break # We are done

            # 3. Store the start of the next group
            nextNode = knode.next
            
            # 4. Detach the k-group to reverse it
            knode.next = None
            
            # 5. Reverse the k-group
            # After reverse, 'knode' is the new head, 'temp' is the new tail
            self.reverse(temp) 

            # 6. Re-link the reversed groups
            if temp == head:
                # If this was the first group, update the main list head
                head = knode
            else:
                # Link the previous group's tail to the new group's head
                prevl.next = knode

            # 7. Update pointers for the next iteration
            prevl = temp     # The tail of this group is the new 'prevl'
            temp = nextNode  # Move to the start of the next group
            
        return head