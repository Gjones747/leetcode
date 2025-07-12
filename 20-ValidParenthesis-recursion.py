class Solution:
    def isValid(self, s: str) -> bool:
        if s.count("(") != s.count(")") or s.count("[") != s.count("]") or s.count("{") != s.count('}'):
            return False
        print(self.check_substring(s))

        if self.check_substring(s) == None:
            return True
        else:
            return False

    def check_substring(self, s: str):
        for i in range(len(s)):
            if s[i] == "(":
                check = s[(i+1):]
                count = 1
                for r in range(len(check)):
                    if check[r] == "(":
                        count = count + 1
                    if check[r] == ")":
                        count = count - 1
                    if count == 0:
                        newstring = check[:r]
                        remaining = check[(r+1):]
                        print(newstring+remaining)
                        if newstring.count("(") != newstring.count(")") or newstring.count("[") != newstring.count("]") or newstring.count("{") != newstring.count('}'):
                            return False
                        return self.check_substring(newstring+remaining)
                        
                return False
            
            if s[i] == "[":
                check = s[(i+1):]
                count = 1
                for r in range(len(check)):
                    if check[r] == "[":
                        count = count + 1
                    if check[r] == "]":
                        count = count - 1
                    if count == 0:
                        newstring = check[:r]
                        remaining = check[(r+1):]
                        print(newstring+remaining)
                        if newstring.count("(") != newstring.count(")") or newstring.count("[") != newstring.count("]") or newstring.count("{") != newstring.count('}'):
                            return False
                        return self.check_substring(newstring+remaining)
                        
            
                return False

            if s[i] == "{":
                check = s[(i+1):]
                count = 1
                for r in range(len(check)):
                    if check[r] == "{":
                        count = count + 1
                    if check[r] == "}":
                        count = count - 1
                    if count == 0:
                        newstring = check[:r]
                        remaining = check[(r+1):]
                        print(newstring+remaining)
                        if newstring.count("(") != newstring.count(")") or newstring.count("[") != newstring.count("]") or newstring.count("{") != newstring.count('}'):
                            return False
                        return self.check_substring(newstring+remaining)
                        
                return False




test = Solution()

print(test.isValid("([()])([[]])([])()]"))