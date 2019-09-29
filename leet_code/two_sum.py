import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        list_len = len(nums)

        for i in range(list_len-1):
            j = i+1
            while j < list_len:
                if nums[i] + nums[j] == target:
                     return [i, j]
                j += 1
