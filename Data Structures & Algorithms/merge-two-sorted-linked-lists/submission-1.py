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
        
        before_head = prev = ListNode()

        while list1 or list2:
            if not list1:
                prev.next = list2
                return before_head.next
            
            if not list2:
                prev.next = list1
                return before_head.next

            if list1.val <= list2.val:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next
            prev = prev.next
        
        return before_head.next
