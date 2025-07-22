package leetcode

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

type ListNode struct {
	Val  int
	Next *ListNode
}

func deleteDuplicates(head *ListNode) *ListNode {
	curr := head

	if curr == nil {
		return head
	}
	for curr.Next != nil {
		next := curr.Next

		if curr.Val == curr.Next.Val {
			curr.Next = next.Next
		} else {
			curr = curr.Next
		}
	}
	return head
}
