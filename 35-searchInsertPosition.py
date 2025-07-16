class Solution:
    def searchInsert(self, nums:[int], target: int) -> int:
        upper = len(nums)
        lower = 0 

        if target > nums[-1]:
            return len(nums)
        if target < nums[0]:
            return 0

        while upper > lower:
            check = ((upper - lower )//2) + lower
            if nums[check] == target:
                return check

            if nums[check] > target and nums[check-1] < target:
                return check
            
            if nums[check] > target:
                upper = check
            elif nums[check]<target:
                lower = check

test = Solution()
print(test.searchInsert([-1,3,5,6], 0))
        
