class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        right = 0

        left = 0
        window = nums[:right]
        minWindow = nums
        reachedNum = False
        sum = 0

        while right < len(nums):
            right += 1
            window = nums[left:right]
            sum += window[-1]

            while sum >= target:
                window = nums[left:right]
                reachedNum = True
                if len(window) <= len(minWindow):
                    minWindow = window

                left += 1
                sum -= window[0]
        
        if reachedNum == False:
            return 0
        return len(minWindow)