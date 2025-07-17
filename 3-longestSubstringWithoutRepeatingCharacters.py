class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        previous = {}
        longest = 0
        checkLongest = 0
        i = 0
        while i < len(s):
            if s[i] not in previous:
                checkLongest+=1
                previous[s[i]] = i
            else:
                lastIndex = previous[s[i]]
                i = lastIndex + 1
                previous = {}
                previous[s[i]] = i
                checkLongest = 1
            if checkLongest > longest:
                    longest = checkLongest
            i += 1
        return longest





test = Solution()
print(test.lengthOfLongestSubstring("dvdf"))