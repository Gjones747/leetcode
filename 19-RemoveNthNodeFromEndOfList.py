# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        # creates a copy of the list head then cycles through to find the total length of the linked list
        check = head
        list_length = 0
        while check:
            check = check.next
            list_length += 1
        
        #then iterates through the list and removes the element Nth from the end (list_length - 1)
        k = 0
        while head:
            if k != (list_length - n):
                curr.next = ListNode(head.val)
                curr = curr.next
                head = head.next
            else:
                head = head.next
            k+=1

        
        return dummy.next