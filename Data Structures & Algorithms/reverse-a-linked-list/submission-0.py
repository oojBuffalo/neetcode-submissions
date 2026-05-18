# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: length 0
        if not head:
            return None
        
        # Base case: head node
        n = head
        n_plus_1 = head.next
        head.next = None

        # Inductive step: all subsequent nodes
        while n_plus_1:
            n_plus_2 = n_plus_1.next  # Store reference to n+2 node before overwrite
            n_plus_1.next = n         # Update reference to n+1 node's next node to n node
            n = n_plus_1              # Update reference to n node to n+1 node
            n_plus_1 = n_plus_2       # Update reference to n+1 node to n+2 node  
            
        return n