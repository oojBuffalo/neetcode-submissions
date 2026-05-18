# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        if not list1 and list2:
            return list2
        if list1 and not list2:
            return list1
        
        prev = None
        head = None
        
        curr_l1 = list1
        curr_l2 = list2

        while curr_l1 or curr_l2:
            if not curr_l1:
                prev.next = curr_l2
                return head
            
            if not curr_l2:
                prev.next = curr_l1
                return head

            if curr_l1.val <= curr_l2.val:
                if not prev:
                    prev = head = curr_l1
                    curr_l1 = curr_l1.next
                    continue
                else:
                    prev.next = curr_l1
                    prev = curr_l1
                    curr_l1 = curr_l1.next
            else:
                if not prev:
                    prev = head = curr_l2
                    curr_l2 = curr_l2.next
                    continue
                else:
                    prev.next = curr_l2
                    prev = curr_l2
                    curr_l2 = curr_l2.next
        return head
