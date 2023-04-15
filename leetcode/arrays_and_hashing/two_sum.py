"""
Given an array of integers nums and an integer target, return indices 
of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

You can return the answer in any order.
"""

# nums, target = [2,7,11,15], 9
nums, target = [3,2,4], 6
# nums, target = [3,3], 6
# nums, target = [3,2,3], 6
# nums, target = [2,5,5,11], 10
# nums, target = [-3,4,3,90], 0

array_size = len(nums)

def two_sum(nums, target):
    # Solution 1
    # Time complexity: O(n^2)
    # Space complexity: O(n)
    # for i in range(0, array_size-1):
    #     for j in range(i+1, array_size):
    #         if (nums[i] + nums[j] == target):
    #             return (i, j)


    # Solution 2
    # Time complexity: O(n)
    # Space complexity: O(n)
    dictionary = {}
    for key, value in enumerate(nums):
        left = target - nums[key]
        if left in dictionary:
            return [dictionary[left], key]
        dictionary[value] = key

two_sum(nums, target)