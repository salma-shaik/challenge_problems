'''

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4


Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104

'''
from typing import List

class Solution:

    def searchInsert(self, nums: List[int], target: int) -> int:
        pos = 0
        for idx, num in enumerate(nums):
            if num == target:
                pos = idx
            elif target > num:
                pos = idx + 1
        return pos

# result = Solution.searchInsert(Solution(), [1,3,5,6], target = 5)
# print(result)

'''
Input: nums = [1,3,5,6], target = 2
Output: 1
'''
# result = Solution.searchInsert(Solution(), [1,3,5,6], target = 2)
# print(result)

'''
Input: nums = [1,3,5,6], target = 7
Output: 4
'''
result = Solution.searchInsert(Solution(), [1,3,5,6], target = 7)
print(result)


"""
TOP:

    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start < end:
            mid = math.floor((start + end) / 2)
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                end = mid - 1
            elif target > nums[mid]:
                start = mid + 1
        if target <= nums[start]:
            return start
        else:
            return start + 1

"""