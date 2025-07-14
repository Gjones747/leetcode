class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        
        return j


test = Solution()
test.removeElement([1, 2, 2, 3, 3, 3, 4, 5, 6, 7, 7], 3)