# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # turn linked lists into strings
        first = ""
        second = ""
        while l1:
            first = str(l1.val) + first
            l1 = l1.next
        
        while l2:
            second = str(l2.val) + second
            l2 = l2.next
        #add together to find answer
        answer = int(first) + int(second)
        answer = str(answer)
        dummy = ListNode()
        curr = dummy
        # turn answer into string then traverse backwards to add to linked list
        for i in range(len(answer)):
            val = len(answer) -1 - i
            curr.next = ListNode(int(answer[val]))
            curr = curr.next

        return dummy.next
            
        
        