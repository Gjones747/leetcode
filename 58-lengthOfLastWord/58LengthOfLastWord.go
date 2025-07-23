package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Println(lengthOfLastWord("   fly me   to   the moon  "))
}

func lengthOfLastWord(s string) int {
	s = strings.TrimSpace(s)
	parts := strings.Split(s, " ")

	return len(parts[len(parts)-1])
}
