# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # dummy always points to the head node
        dummy = ListNode()
        # current iterates across the dummy list without changing the head
        cur = dummy

        while list1 and list2:
            if list1.val < list2.val:
                cur.next = ListNode(list1.val)
                cur = cur.next
                list1 = list1.next
            else: 
                cur.next = ListNode(list2.val)
                cur = cur.next
                list2 = list2.next 
        
        # add whatever is left to the end of the linked list
        while list1:
            cur.next = ListNode(list1.val)
            cur = cur.next
            list1 = list1.next
        while list2:
            cur.next = ListNode(list2.val)
            cur = cur.next
            list2 = list2.next

        return dummy.next
