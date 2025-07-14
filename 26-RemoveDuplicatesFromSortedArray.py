class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        last = None
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j+=1

        print(nums)
        return j


test = Solution()
print(test.removeDuplicates([1,1,2]))



