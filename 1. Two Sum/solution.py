
def twoSum(nums, target): 
    """
     @param nums The input that is an array of integers
     @param target The the target sum, calculated from the input array
    """

    for i in range(0,len(nums)):
        for j in range(1,len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]


def twoSumFast(nums, target):
    """
     @param nums The input that is an array of integers
     @param target The the target sum, calculated from the input array
     * The algorithm should be less than O(n^2) time complexity
    """

    nums.sort() # O(n log n)

    
print(twoSum([2,7,11,15], 9))
print(twoSum([3,2,4], 6))
print(twoSum([3,3], 6))