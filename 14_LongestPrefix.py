class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        index = 0
        try:
            for letter in range(len(strs[0])):
                true = 0
                for word in strs:
                    if word[letter] == strs[0][letter]:
                        true+=1
                if (true == len(strs)):
                    index+=1
                else:
                    break
                true = 0
        except:
            pass
        print(strs[0][0:index])
        
        print(index)
test = Solution()
test.longestCommonPrefix(["cir", "car"])