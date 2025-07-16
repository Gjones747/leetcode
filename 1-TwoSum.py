class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previous = {}
        for i, num in enumerate(nums):
            if i != 0:
                compliment = target - num
                if compliment in previous:
                    return [previous[compliment], i]
            previous[num] = i

        
