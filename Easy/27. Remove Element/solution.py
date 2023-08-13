class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        curr = 0
        i = 0
        while i < len(nums):
            if val == nums[i]:
                del nums[i]
                i -= 1
            else:
                curr = i        
            i += 1

        return curr + 1