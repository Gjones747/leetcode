package main

import "fmt"

func main() {
	fmt.Println(minSubArrayLen(7, []int{1, 2, 3, 4, 5}))
}

func minSubArrayLen(target int, nums []int) int {
	left := 0
	right := 0
	window := make([]int, 0, len(nums))
	minWindow := make([]int, 0, len(nums))
	subLength := len(nums)
	total := 0

	for right < len(nums) {
		right += 1
		window = nums[left:right]
		total += window[len(window)-1]
		for total >= target {
			window = nums[left:right]

			if len(window) <= subLength {
				minWindow = window
				subLength = len(minWindow)

			}

			left += 1
			total -= window[0]
		}

	}

	return len(minWindow)

}
