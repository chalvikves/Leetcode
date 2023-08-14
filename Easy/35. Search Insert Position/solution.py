class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            mid_value = nums[mid]
            if mid_value == target:
                return mid
            elif mid_value > target:
                right = mid - 1
            else:
                left = mid + 1
            
        return left