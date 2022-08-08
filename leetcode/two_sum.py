'''
 Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

'''

class TwoSum:

    def two_sum(self, nums, target):
        result_list = []
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if (nums[i] + nums[j] == target):
                    result_list.append(i)
                    result_list.append(j)
        return result_list

class Solution:
    # nums = [3,2,3]
    # target = 6
    nums = [2,7,11,15]
    target = 9
    count = 0

    two_sum_obj = TwoSum()
    print(two_sum_obj.two_sum(nums, target))