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

	check := make(map[int]int)

	for curr.Next != nil {
		next := curr.Next

		check[curr.Val] += 1

		_, isKeyInMap := check[next.Val]

		if isKeyInMap {
			curr.Next = next.Next
		} else {
			curr = curr.Next

		}

	}

	return head
}
