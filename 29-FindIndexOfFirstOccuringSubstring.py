#this works but it is kinda cheese
#class Solution:
#    def strStr(self, haystack: str, needle: str) -> int:
#       return haystack.find(needle)

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        substringLength = len(needle)
        for i in range(len(haystack)-substringLength+1):
            if haystack[i:substringLength+i] == needle:
                return i
        
        return -1

test = Solution()
print(test.strStr("a", "a"))