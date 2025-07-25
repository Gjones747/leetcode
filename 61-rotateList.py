# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def rotateRight(self, head, k: int):
        listMap = {}
        curr = head
        i = 0
        while curr:
            listMap[i] = curr.val
            curr = curr.next
            i+=1 
        curr = head
        if i != 0:
            startIndex = k % i
        else:
            return
        for i in range(len(listMap)-startIndex, len(listMap)):
            curr.val = listMap[i]
            curr = curr.next

        for i in range(len(listMap)-startIndex):
            curr.val = listMap[i]
            curr = curr.next


        return head
        



