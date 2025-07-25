package main

import "fmt"

func main() {
	fmt.Println(plusOne([]int{8, 9, 9, 9}))
}

func plusOne(digits []int) []int {

	for i := len(digits) - 1; i >= 0; i-- {
		if digits[i] < 9 {
			digits[i] += 1
			return digits
		}

		digits[i] = 0
	}

	digits = append([]int{1}, digits...)
	return digits
}
