class Solution:
    def mySqrt(self, x: int) -> int:
        upper = x
        lower = 0
        answer = None

        while not answer:
            check = ((upper-lower)//2)+lower
            if (check*check) == x or ((((check+1) * (check+1)) > x) and ((check*check)<x)):
                return check
            if (check*check) > x:
                upper = check
            elif (check*check) < x:
                lower = check

test = Solution()
print(test.mySqrt(1))