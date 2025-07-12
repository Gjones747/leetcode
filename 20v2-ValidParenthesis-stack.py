class Solution:
    def isValid(self, s: str) -> bool:
        match = {
            "(":")",
            "[":"]",
            "{":"}"
        }

        stack = []
        try:
            for i in s:
                if i in match.values() and stack and stack[-1] == i:
                    stack.pop()

                else:
                    stack.append(match[i])
        except:
            return False

        if not stack:
            return True
        else:
            return False        
                







test = Solution()

print(test.isValid("([()])([[]])([])())"))