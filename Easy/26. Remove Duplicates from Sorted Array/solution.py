class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[curr-1]:
                nums[curr] = nums[i]
                curr += 1

        return curr
    
def main():
    print(Solution().removeDuplicates([1,1,2]))
    print(Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
    
if __name__ == '__main__':
    main()