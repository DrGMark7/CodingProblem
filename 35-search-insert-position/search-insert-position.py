class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            elif target not in nums and target < min(nums):
                return 0
            elif i == len(nums)-1:
                return len(nums)
            elif nums[i+1] > target and target > nums[i]:
                return i+1
            elif target not in nums and target > max(nums):
                return len(nums)